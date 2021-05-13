n = int(input())
a = [int(i) for i in input().split()]

sm = sum(a)
acc = [0]
for i in range(n):
  acc.append(acc[-1] + a[i])

ans = 10000000000
for i in range(1,n):
  ans = min(ans,abs(sm - acc[i] * 2))
print(ans)
