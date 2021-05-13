a=int(input())
b=[]
for _ in range(a):
    b.append(list(map(str,input().split())))
ans=0
for i in range(a):
    if b[i][1]=='JPY':
        ans+=int(b[i][0])
    else:
        ans+=float((b[i][0]))* 380000
print(ans)