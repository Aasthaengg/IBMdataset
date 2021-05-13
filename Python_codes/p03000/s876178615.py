n, x = map(int, input().split())
l = list(map(int, input().split()))

d = 0
count = 1
for v in l:
    dv = d + v
    # print(dv)
    
    if dv > x:
        break
    
    count += 1
    d += v

print(count)