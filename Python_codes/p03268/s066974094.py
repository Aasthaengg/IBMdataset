[n,k] = [int(i) for i in input().split()]

if k % 2 == 0:
    mod = k // 2
    count_mod = 0
    count = 0
    for i in range(1,n+1):
        if i % k == 0:
            count += 1
            #print("zero",i)
        elif i % k == mod:
            count_mod += 1
            #print("mod",i)
    #print(count,count_mod)
    print(count**3 + count_mod ** 3)
else:
    count = 0
    for i in range(1,n+1):
        if i % k == 0:
            count += 1
    print(count ** 3)
