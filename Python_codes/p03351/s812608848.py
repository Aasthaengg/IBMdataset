a,b,c,d = map(int,input().split())
dist1 = abs(c-a)
dist2 = abs(a-b)
dist3 = abs(c-b)
if dist1<=d or (dist2<=d and dist3<=d):
    print('Yes')
else:
    print('No')