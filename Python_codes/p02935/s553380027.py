N=int(input())
v=list(map(int,input().split()))
while len(v)!=1:
    v=sorted(v)
    x=(v[0]+v[1])/2
    v.pop(0)
    v.pop(0)
    v.append(x)
print(v[0])