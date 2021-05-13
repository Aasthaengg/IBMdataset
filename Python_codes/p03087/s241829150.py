from sys import stdin
def input():
    return stdin.readline().strip()

def main():
    n, q = map(int, input().split())
    s = input()

    # Cumulative Sum
    cs = [0] * n
    for i in range(1, n):
        if s[i-1] == 'A' and s[i] == 'C':
            cs[i] = cs[i-1] + 1
        else:
            cs[i] = cs[i-1]

    ans = [0] * q
    for lap in range(q):
        l, r = map(int, input().split())
        ans[lap] = cs[r-1] - cs[l-1]

    for i in ans:
        print(i)

main()