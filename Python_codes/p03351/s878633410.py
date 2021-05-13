a,b,c,d=map(int,input().split())

if (max(a,b)-min(a,b)) <= d and (max(c,b)-min(c,b)) <= d:
    print('Yes')
elif (max(a,c)-min(a,c)) <= d:
    print('Yes')
else:
    print('No')