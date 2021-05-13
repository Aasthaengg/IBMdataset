n,k,x,y = [int(input()) for i in range(4)]

total = 0
day = 0
for i in range(n):
    day += 1
    if day <= k:
        total += x
    else:
        total += y
print(total)
