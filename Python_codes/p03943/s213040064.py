a,b,c = map(int, input().split())
tmp = a + b + c

if (tmp - a == tmp/2 or tmp - b == tmp/2 or tmp - c == tmp/2):
    print('Yes')
else:
    print('No')
