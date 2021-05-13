x,y = map(int, input().split())
c = 1
for i in range(1000000000):
    x *= 2
    if (x<=y):
        c += 1
    else:
        break
    
print(c)