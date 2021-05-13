a, b, c = map(int,input().split())

i = 3
if a==b:
    i-=1
if b==c:
    i-=1
if c==a:
    i-=1
if not i:
    i=1
print(i)