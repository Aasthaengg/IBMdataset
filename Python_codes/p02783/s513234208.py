a, b = map(int, input().split())
c = a%b
if c!=0:
    print((a//b)+1)
elif c==0:
    print(a//b)
