n=int(input())
st=[list(input().split()) for _ in range(n)]
x=input()

ans=0
flag=False
for i in range(n):
    if flag:
        ans+=int(st[i][1])
    if st[i][0]==x:
        flag=True
print(ans)