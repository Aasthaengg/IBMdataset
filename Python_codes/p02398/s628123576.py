p = 0
a,b,c = map(int,input().split())
x=a
while True:
    if c%x==0:
        p += 1
    x += 1
    if x > b:
        break

print(p)
