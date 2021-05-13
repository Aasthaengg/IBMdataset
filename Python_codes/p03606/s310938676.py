N=int(input())
l=[]
tmp=0
for i in range(N):
    l.append(list(map(int,input().split())))
for i in range(N):
    tmp+=abs(l[i][0]-l[i][1])+1
print(tmp)
