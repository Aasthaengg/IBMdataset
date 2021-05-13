a, b, k = map(int, input().split())
chk = 0
i = 100
while i > 0:
    if a%i==0 and b%i==0:
        chk += 1
        if chk == k:
            print(i)
            exit()
        else:
            pass
    i -= 1