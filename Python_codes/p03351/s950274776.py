a,b,c,d = map(int,input().split())
if abs(c-a) <= d:
    print('Yes')
elif d < abs(c-a) <=2*d and abs(c-b) <=d and abs(b-a) <=d:
    print('Yes')
else:
    print('No')