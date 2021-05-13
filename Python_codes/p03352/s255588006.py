x = int(input())

ans = 0
for i in range(1,32):
    for p in range(2,10):
        y = i**p
        if y > 1000:
            break
        if ans < y <= x:
            ans = y
print(ans)