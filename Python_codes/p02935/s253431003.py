N=int(input())
v=sorted(list(map(int,input().split())))
s=v[0]
for i in range(N-1):
    s=(s+v[i+1])/2
print(s)

