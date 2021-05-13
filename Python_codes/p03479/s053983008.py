x,y = map(int,(input().split()))
now = x
c = 1
while now*2 <= y:
    now *= 2
    c += 1
print(c)