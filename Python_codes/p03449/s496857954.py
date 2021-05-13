N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

key=sum(a[0:N-1])+b[-1]
for i in range(0,N):
  Key=sum(a[0:i+1])+sum(b[i:N])
  key=max(key,Key)
print(key)