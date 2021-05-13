K = int(input())

if K % 2 == 0 or K % 5 == 0:
    print(-1)
else:
    x = 7 % K
    for i in range(1, K + 1):
        if x == 0:
            print(i)
            break
        x = (x * 10 + 7) % K