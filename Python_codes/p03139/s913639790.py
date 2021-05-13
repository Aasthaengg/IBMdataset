n,a,b=map(int, input().split())
c=min(a,b)
d=max(a,b)
if n-d<c:
    d=c-(n-d)
else:
    d=0
print(c,d)
