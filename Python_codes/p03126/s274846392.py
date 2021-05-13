n,m=map(int,input().split())
a=[]
k=[]
while True:
    try:
        dk,*d=list(map(int,input().split()))
        a.append(d)
        k.append(dk)
    except:
        break;
ans=set(a[0])
for i in range(1,n):
  ans=ans&set(a[i])

print(len(ans))