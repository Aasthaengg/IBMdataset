import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
mod = 10**9 + 7

n, k = map(int, input().split())
s = list(input())
s[k - 1] = s[k - 1].lower()
print("".join(s))


