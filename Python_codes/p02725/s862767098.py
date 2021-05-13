k,n=map(int,input().split())
a=list(map(int,input().split()))
a.append(a[0]+k)
cnt=0

for i in range(n):
  cnt=max(cnt,a[i+1]-a[i])
print(k-cnt)