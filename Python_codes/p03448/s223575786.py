a = int(input())
b = int(input())
c = int(input())
x = int(input())
count=0

for s in range(a+1):
    if s*500 == x:
        count += 1
    for t in range(b+1):
        if s*500 + t*100 == x and t != 0:
            count += 1
        for u in range(c+1):
            if s*500 + t*100 + u*50 == x and u != 0:
                count += 1

print(count)