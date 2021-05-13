N=int(input())
*A,=map(int,input().split())
ans=[]
for a in A:
    if len(ans)<a-1:
        ans=[-1]
        break
    else:
        ans.insert(a-1,a)

for x in ans:
    print(x)