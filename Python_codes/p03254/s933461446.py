N,x=map(int,input().split())
a=list(map(int,input().split()))
a_sort=sorted(a,reverse=False)
tot=0
if sum(a)==x:
    print(len(a))
elif sum(a)<x:
    print(len(a)-1)
else:
    for i in range(N):
        tot+=a_sort[i]
        if tot==x:
            print(i+1)
            break
        elif tot<x:
            pass
        elif tot>x:
            print(i)
            break