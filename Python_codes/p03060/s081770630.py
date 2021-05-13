N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

ans = 0
for i, j in zip(V,C):
  if i - j > 0:
    ans += i - j
print(ans)