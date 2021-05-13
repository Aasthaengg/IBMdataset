n,k=map(int, input().split())
a=list(map(int, input().split()))

for t in range(k):
      ok=True
      b=[0]*n
      for i in range(n):
            left=max(0,i-a[i])
            b[left]+=1
            if i+a[i]+1 <= n-1:
                  right=i+a[i]+1
                  b[right]-=1
      for i in range(1,n):
            b[i]=b[i-1]+b[i]
      for i in range(n):
            if a[i]!=b[i]:
                  ok=False
            a[i]=b[i]
      if ok==True:
            break

print(*a)

