n=int(input())
a=[int(j) for j in input().split()]
a.sort()
ans=[]
p=a[0]
q=a[-1]
for i in a[1:-1]:
    if i<0:
        ans.append([q,i])
        q-=i
    else:
        ans.append([p,i])
        p-=i
ans.append([q,p])
print(q-p)
for i,j in ans:
    print(i,j)
