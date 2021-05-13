l, r, d = map(int, input().split())

now = d

count = 0

while now <= r:

    if now >= l:
        count += 1
    
    now += d

print(count)