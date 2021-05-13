N = int(input())
A = list(map(int, input().split()))

ans = 0
for Ai in A:
  ans += 1/Ai

print(1/ans)
