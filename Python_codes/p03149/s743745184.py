a, b, c, d = map(int,input().split())

l=[1,9,7,4]
if a in l and b in l and c in l and d in l and len(set([a,b,c,d]))==4:
    print('YES')
else:
    print('NO')