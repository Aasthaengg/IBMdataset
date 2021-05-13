d=int(input())
c= list(map(int, input().split()))
D= [list(map(int, input().split())) for i in range(d)]
t= [int(input()) for i in range(d)]

ans=[0]*(d+1)
v=sum(c)

# 最後にどの試験がいつ行われたか？
PL=[0]*26

for i in range(d):
    x=t[i]-1
    ans[i+1]+=ans[i]+D[i][x]
    PL[x]=i+1
    for j in range(26):
        ans[i+1]-=(i+1-PL[j])*c[j]

for i in range(1,d+1):
    print(ans[i])
