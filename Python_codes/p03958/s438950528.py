K,T=map(int,input().split())
a=list(map(int,input().split()))

maxi=max(a)
other = sum(a)-maxi
#print(maxi,other)

if maxi<=other:
    print(0)
else:
    print(maxi-other-1)
