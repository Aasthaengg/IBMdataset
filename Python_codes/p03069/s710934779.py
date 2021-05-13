from sys import stdin

def main():
    input = stdin.readline

    n = int(input())
    s = input()
    a = [[0, 0] for _ in range(n)]
    if s[0] == '.':
        a[0][0] = 1
    else:
        a[0][1] = 1
    for i in range(1, n):
        if s[i] == '.':
            a[i][0] = a[i - 1][0] + 1
            a[i][1] = a[i - 1][1]
        else:
            a[i][0] = a[i - 1][0]
            a[i][1] = a[i - 1][1] + 1
    min = a[-1][0] if a[-1][0] < a[-1][1] else a[-1][1]
    for i in range(n):
        if min > a[-1][0] - a[i][0] + a[i][1]:
            min = a[-1][0] - a[i][0] + a[i][1]
    print(min)
main()