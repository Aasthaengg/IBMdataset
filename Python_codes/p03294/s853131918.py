# C - Modulo Summation

N = int(input())
A = list(int(a) for a in input().split())

ans = 0
for a in A:
    ans += a-1

print(ans)