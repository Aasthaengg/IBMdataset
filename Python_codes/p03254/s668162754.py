N,X,*A=map(int,open(0).read().split())
c=0
for a in sorted(A):
    X-=a
    if X<0:
        break
    c+=1
print(c-(X>0))