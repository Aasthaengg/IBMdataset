n,m=map(int, input().split())
a=list(map(int, input().split()))
bc_list=[]
for i in range(m):
    b,c=map(int, input().split())
    bc_list.append([b,c])

a.sort()
import operator
bc_list.sort(key=operator.itemgetter(1),reverse=True)

s=0

ans=0
for i in range(m):
    for j in range(s,s+bc_list[i][0]):
        if j>=n:
            break
        if a[j]<bc_list[i][1]:
            ans+=bc_list[i][1]
            s+=1
        else:
            break

for i in range(s,n):
    ans+=a[i]
print(ans)