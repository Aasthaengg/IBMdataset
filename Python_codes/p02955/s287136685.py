n,k=map(int,input().split())
a=list(map(int,input().split()))
a_sum=sum(a)
def devisor(x):
    lst=[]
    i=1
    y=x
    while i**2<=y:
        if x%i==0:
            lst.append(i)
            if i!=x//i:
                lst.append(x//i)
        i+=1
    lst.sort()
    return lst
re=devisor(a_sum)
re.sort(reverse=True)
for u in re:
    w=[]
    for v in a:
        w.append(v%u)
    w.sort()
    b=sum(w)
    count=0
    for i in range(b//u):
        w[-i-1]-=u
    for i in w:
        if i>=0:
            count+=i
        else:
            break
    if count<=k:
        print(u)
        break