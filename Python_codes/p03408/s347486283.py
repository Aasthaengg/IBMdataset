N=int(input())
plus=[input() for i in range(N)]
M=int(input())
minus=[input() for i in range(M)]
S=list(set(plus+minus))
ans=0
for i in S:
    point=0
    point=plus.count(i)-minus.count(i)
    ans=max(ans,point)
print(ans)