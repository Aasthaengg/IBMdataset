n = int(input())
a = list(map(int,input().split()))
avg = sum(a)/n
difmin = 10**18
for i in range(n):
  if difmin>abs(a[i]-avg):
    difmin = abs(a[i]-avg)
    ans = i
print(ans)
