a,b,c = map(int,input().split())
l=sorted([a,b,c])
print(l[2]-l[1]+l[1]-l[0])
