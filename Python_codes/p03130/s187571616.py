li=[0]*4

for i in range(3):
    a,b=map(int,input().split())
    li[a-1]+=1
    li[b-1]+=1

if li.count(1)==2 and li.count(2)==2:
    print("YES")
else:
    print("NO")