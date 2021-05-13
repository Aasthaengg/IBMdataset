N,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
if sum(a)==x:
    print(N)
else:
    a.sort()
    s=0
    i=0
    while True:
       s+=a[i]
       if i==N-1 and s!=x:
           print(N-1)
           break
       if s>x:
           print(i)
           break
       i+=1
       if i>=N:
           print(N)
           break

