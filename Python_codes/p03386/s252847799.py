a,b,k=map(int,input().split())
ha=[i for i in range(a,a+k) if i<=b]
o=[i for i in range(b,b-k,-1) if i>=a]
wa=set(ha+o)
wa=sorted(list(wa))
for i in wa:
    print(i)