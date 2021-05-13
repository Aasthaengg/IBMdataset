x,y = map(int, input().split())
i = 0
c = 0
while c <= y:
    i += 1
    c  = x * (2**i)
print(i)