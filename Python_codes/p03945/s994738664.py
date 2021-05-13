import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

S = list(input())
ans = 0
for i in range(1, len(S)):
    if S[i - 1] != S[i]:
        ans += 1

print (ans)