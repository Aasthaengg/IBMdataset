D=int(input())
c=list(map(int, input().split()))
s=[list(map(int, input().split()))  for i in range(D)]
t=[int(input()) for i in range(D)]

d=[0]*(26)
v=[0]*(D+1)


for i in range(D):
    v[i]=s[i][t[i]-1]
    d[t[i]-1]=-1
    sb=0      
    for j in range(26):
        d[j]+=1 
        sb+=d[j]*c[j]
                   
    v[i]+=v[i-1]-sb
    print(v[i])