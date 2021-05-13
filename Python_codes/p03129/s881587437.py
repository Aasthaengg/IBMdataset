l=[]
n,k=map(int,input().split())
for i in range(1,n+1,2):
    l.append(i)

if k<=len(l):
    print("YES")
else:
    print("NO")


