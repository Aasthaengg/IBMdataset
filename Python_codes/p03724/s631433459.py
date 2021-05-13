n,m=map(int,input().split())
#n<=10**5

tree=[0]*n

for _ in range(m):
    x,y=map(int,input().split())
    tree[x-1]+=1
    tree[y-1]+=1

for item in tree:
    if item%2==1:
        print("NO")
        exit()

print("YES")

