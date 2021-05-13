l, r = map(int,input().split())

a = 0
while a < l:
    a += 2019
if r - a >= 2019:
    print(0)
    exit()

d = 2019
for i in range(l, r+1):
    for j in range(l, r+1):
        if i == j:
            continue
        d = min(d, i*j % 2019)

print(d)