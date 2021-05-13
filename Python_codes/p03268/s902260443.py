n , k = map(int,input().split())
if k % 2 == 1:
    cou = 0
    for i in range(1,n+1):
        if i % k == 0:
            cou += 1
    print(cou**3)
elif k % 2 == 0:
    cou = 0
    cou2 = 0
    for i in range(1,n+1):
        if i % k == 0:
            cou += 1
        elif i % k == k//2:
            cou2 += 1
    print(cou**3+cou2**3)