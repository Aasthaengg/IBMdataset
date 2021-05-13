a,b=map(int,input().split())
d=b-a
tree=[]
tr=0
for i in range(1,1000):
    tr+=i
    tree.append(tr)
#print(tree)
#print(tree[d-1])
print(tree[d-1]-b)