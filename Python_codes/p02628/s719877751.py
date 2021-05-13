N,K =  [int(i) for i in input().split()]
P = [int(i) for i in input().split()]

P.sort()
ans = 0
for i in range(K):
  ans += P[i]
print(ans)