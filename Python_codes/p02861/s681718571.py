import itertools

n=int(input())
l=[]
for i in range(n):
    x=[int(j) for j in input().rstrip().split()]
    l.append(x)


cnt=0
ans=0
num=[i for i in range(n)]
for i in itertools.permutations(num,n):
    cnt+=1
    for j in range(n-1):
        ans+=((l[i[j]][0]-l[i[j+1]][0])**2+(l[i[j]][1]-l[i[j+1]][1])**2)**0.5
print(ans/cnt)
