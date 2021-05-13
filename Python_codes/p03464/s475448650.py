K=int(input())
A=list(map(int,input().split()))
l,h=2,2
for a in A[::-1]:
    l=-(-l//a)*a
    h=(h//a+1)*a-1
    if l>h:
        l=h=-1
        break
if l==h==-1:
    print(-1)
else:
    print(l,h)