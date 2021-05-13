n=int(input())
v=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
vc=[]
for i in range(n):
    if v[i]-c[i] >0:
        vc.append(v[i]-c[i])
print(sum(vc))

