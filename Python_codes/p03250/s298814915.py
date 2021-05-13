a,b,c = map(int,input().split())
l=sorted([a,b,c])
print(int(str(l[2])+str(l[1]))+l[0])