a, b, c= map(int, input().split())
hantei=0
if a+b==c:
    hantei=1
if a+c==b:
    hantei=1
if b+c==a:
    hantei=1
if hantei==1:
    print('Yes')
else:
    print('No')