a,b,c=map(int,input().split())

l=[a,b,c]

l.sort()

print(int(str(l[2])+str(l[1]))+l[0])