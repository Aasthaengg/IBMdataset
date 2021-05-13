n,x=map(int, input().split())
a=list(map(int, input().split()))
a.sort()

if sum(a)==x:
    print(n)
elif sum(a)<x:
    print(n-1)
else:
    total=0
    cnt=0
    for a_i in a:
        if total+a_i<=x:
            total+=a_i
            cnt+=1
        else:
            break
    print(cnt)
