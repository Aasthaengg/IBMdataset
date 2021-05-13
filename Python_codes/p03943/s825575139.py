a,b,c = map(int,input().split())

li = sorted([a,b,c])
if li[0]+li[1]==li[2]:
    print('Yes')
else:
    print('No')