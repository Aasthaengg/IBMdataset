a,b,k = map(int,input().split())
i = 101
j = 0
while True:
    i -= 1
    if a % i == 0 and b % i == 0:
        j += 1
        if j == k:
            print(i)
            break