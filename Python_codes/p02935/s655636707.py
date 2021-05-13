n = int(input())
a = list(map(int,input().split()))

a = sorted(a)
ans = []
for i in range(n-1):
  if i ==0:
    ans.append((a[i]+a[i+1])/2)
  else:
    ans.append((ans[i-1]+a[i+1])/2)
print(ans[n-2])
