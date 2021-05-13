n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt=0
for i in range(n):
  f_1 = min(a[i],b[i])
  f_2 = max(0,min(a[i+1],b[i]-a[i]))
  cnt += f_1+f_2
  a[i] -= f_1
  a[i+1] -= f_2
print(cnt)
