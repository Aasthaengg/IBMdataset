n, y = list(map(int, input().split()))
y = y // 1000

if n > y:
    print("-1 -1 -1")
elif 10*n < y:
    print("-1 -1 -1")
else:
    diff = 10*n - y

    for i in range(diff//9 + 1):
        for j in range(diff//5 + 1):
            ans = 9*i + 5*j

            if ans > diff:
                break
            elif (i+j) > n:
                break
            elif ans == diff:
                print(n-(i+j), j, i)
                exit()

    print("-1 -1 -1")