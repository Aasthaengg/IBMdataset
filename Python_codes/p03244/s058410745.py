n=int(input())
v=list(map(int,input().split()))
d1=[0]*(10**5+1)
d2=[0]*(10**5+1)

for i in range(n):
    if i%2==0:
        d1[v[i]]+=1
    else:
        d2[v[i]]+=1
if d1.index(max(d1))==d2.index(max(d2)):
    d1n=sorted(d1,reverse=True)
    d2n=sorted(d2,reverse=True)
    if d1n[1]>d2n[1]:
        print(n-d1n[1]-d2n[0])
    else:
        print(n-d1n[0]-d2n[1])
else:
    print(n-max(d1)-max(d2))