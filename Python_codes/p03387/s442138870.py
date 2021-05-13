a,b,c = map(int, input().split())
m = max(a, max(b, c))
if (a+b+c)%2 != (3*m)%2:
    m += 1
print((3*m-(a+b+c))//2)