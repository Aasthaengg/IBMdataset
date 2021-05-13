a,b = (int(x) for x in input().split())
s = 0
d = b - a

for i in range(d):
    s += i

print(s-a)
