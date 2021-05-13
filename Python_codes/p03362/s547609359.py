n = int(input())
l = [11,31,41,61,71]
if n == 5:
    print(*l)
    exit()
for i in range(81,60000,10):
    check = True
    for j in range(3,int(i**0.5)+1):
        if i % j == 0:
            check = False
    if check:
        l.append(i)
    if len(l) == n:
        print(*l)
        exit()