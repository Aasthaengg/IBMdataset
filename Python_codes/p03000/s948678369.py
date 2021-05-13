n,x = map(int, input().split())

L = list(map(int, input().split()))

K = [0]
for i in range(len(L)):
  K.append(K[i] + L[i])
ans = 0
for i in range(len(K)):
  if K[i] <= x:
    ans += 1
print(ans)