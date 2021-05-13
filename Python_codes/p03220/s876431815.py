n=int(input())
a,b=map(int,input().split())
h=list(map(int,input().split()))
k=[0]*n
for i in range(n):
  k[i]=b-(a-(0.006*h[i]))
  if k[i]<0:
    k[i]=-1*k[i]
print(k.index(min(k))+1)