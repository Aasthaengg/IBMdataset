n,w=map(int,input().split())
l=[list(map(int,input().split())) for _ in [0]*n]
l1,l2,l3,l4=[],[],[],[]
a=l[0][0]
for i in range(n):
    if l[i][0]==a:
        l1.append(l[i][1])
    elif l[i][0]==a+1:
        l2.append(l[i][1])
    elif l[i][0]==a+2:
        l3.append(l[i][1])
    else:
        l4.append(l[i][1])
l1.sort(reverse=True)
l2.sort(reverse=True)
l3.sort(reverse=True)
l4.sort(reverse=True)
ans=0
for h in range(len(l1)+1):
    for i in range(len(l2)+1):
        for j in range(len(l3)+1):
            for k in range(len(l4)+1):
                if a*h+(a+1)*i+(a+2)*j+(a+3)*k<=w:
                    ans=max(ans,sum(l1[:h])+sum(l2[:i])+sum(l3[:j])+sum(l4[:k]))
print(ans)