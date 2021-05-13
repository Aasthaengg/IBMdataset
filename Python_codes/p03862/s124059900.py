N,x = map(int,input().split())
a=list(map(int,input().split()))
cnt=0
b=[0]*N

#0,2
b[0]=a[0] if a[0]<=x else x
cnt+= a[0]-b[0]

for i in range(1,N):
  b[i] = a[i] if b[i-1]+a[i]<=x else max(0,x-b[i-1])
  cnt += a[i]-b[i]
  
#print(b)
print(cnt)