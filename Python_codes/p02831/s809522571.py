a,b = map(int,input().split())
c = a

for i in range(b):
    if c % b == 0:
        break
    c += a

print(c)