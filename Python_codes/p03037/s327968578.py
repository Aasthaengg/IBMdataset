g=lambda:map(int,input().split())
_,m=g()
ml,mr=0,10**5
for _ in range(m):
    l,r=g()
    ml=max(ml,l)
    mr=min(mr,r)
print([0,mr-ml+1][mr>=ml])
