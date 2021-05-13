n,m=map(int,input().split())
denkyu_switch=[]
res=0
for i in range(m):
    denkyu_switch+=[list(map(int, input().split()))[1:]]
p=list(map(int, input().split()))
for i in range(2**n):
    denkyu = [0] * m
    for j in range(n):
        if i>>j & 1:
            for k in range(m):
                if j+1 in denkyu_switch[k]:
                    denkyu[k]+=1
    denkyu2=[i%2 for i in denkyu]
    if p==denkyu2:
        res+=1
print(res)
