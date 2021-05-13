[n,m] = [int(i) for i in input().split()]
to_acc = [0] * (n+1)
for i in range(m):
  [l,r] = [int(j)-1 for j in input().split()]
  to_acc[l] += 1
  to_acc[r+1] -= 1
acc = [0]
ans = 0
for i in range(n+1):
  acc.append(acc[-1] + to_acc[i])
for i in range(1,n+1):
  if m == acc[i]:
    ans += 1
print(ans)