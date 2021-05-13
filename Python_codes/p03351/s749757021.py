a,b,c,d = map(int,input().split())
bl1 = abs(a-c)<=d
bl2 = abs(a-b)<=d and abs(c-b)<=d
print('Yes' if bl1 or bl2 else 'No')