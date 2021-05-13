n=int(input())
a=list(map(int,input().split()))
ans=0
a_max=max(a)
a_min=min(a)
if a_min>=0:
    adding=a_max
elif a_min<0 and a_max>0:
    if abs(a_max)>=abs(a_min):
        adding=a_max
    else:
        adding=a_min
else:
    adding=a_min
ind=a.index(adding)
proc=[]
for i in range(n):
    ans+=1
    a[i]+=adding
    proc.append([ind+1,i+1])
if adding==a_max:
    for i in range(n-1):
        ans+=1
        a[i+1]+=a[i]
        proc.append([i+1,i+2])
else:
    for i in range(n-1):
        ans+=1
        a[-(i+2)]+=a[-(i+1)]
        proc.append([n-i,n-i-1])
print(ans)
for i in range(len(proc)):
    print(proc[i][0],proc[i][1])