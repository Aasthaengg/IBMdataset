n,x = map(int,input().split())
m = list(int(input()) for i in range(n))
m.sort()

z = sum(m)
s = n

while x > z:
    z += m[0]
    if x >= z:
        s += 1

print(s)