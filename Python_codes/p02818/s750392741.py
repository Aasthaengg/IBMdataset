a,b,c=map(int, input().split())

if c <=a:
    print(a-c,b)
if a < c and b >= c-a:
    print(0,b-(c-a))
if c > a + b:
    print(0,0)