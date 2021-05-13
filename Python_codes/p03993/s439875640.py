n = int (input())
A = [None] + [int(x) for x in input().split()]

ans = 0
for i in range(1, n+1):
  if A[A[i]] == i:
    ans += 1
print(ans //2)