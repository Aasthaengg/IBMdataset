l, r = map(int, input().split())

if r//2019 != l//2019:
    print(0)

else:
    lm = list()
    for i in range(l, r):
        for j in range(i+1, r+1):
            lm.append((i*j)%2019)
    print(min(lm))