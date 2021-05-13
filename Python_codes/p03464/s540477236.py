k = int(input())
ai = reversed([int(x) for x in input().split()])
b = 2; t = 2
f = False
for a in ai:
    b = (((b-1)//a)+1)*a
    t = ((t//a)+1)*a-1
    if b > t:
        f = True
        break
if f:
    print(-1)
else:
    print(b,t)
