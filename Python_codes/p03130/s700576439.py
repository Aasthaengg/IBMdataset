l=[0]*4
for i in range(3):
    a,b=map(int,input().split())
    l[a-1]+=1
    l[b-1]+=1
l.sort()
if l==[1,1,2,2]:print("YES")
else:print("NO")