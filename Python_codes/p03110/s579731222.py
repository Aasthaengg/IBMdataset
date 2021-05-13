N=int(input())
poti=[ input().split() for i in range(N)]
ans=0
for i in poti:
    if i[1]=="JPY":
        ans+=float(i[0])
    else:
        ans+=float(i[0])*380000.0
print(ans)