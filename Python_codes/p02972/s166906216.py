from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    a = [0] + list(map(int, input().split()))
    for i in range(n, 0, -1):
        a[i] = sum(a[i::i]) % 2
    print(sum(a))
    for i in range(1, n + 1):
        if a[i] == 1:
            print(i)
main()