m, k = map(int, input().split())

if 2**m <= k:
    print(-1)

elif m == 0:
    if k == 0:
        print(0, 0)
    else:
        print(-1)

elif m == 1:
    if k == 0:
        print(0,0,1,1)
    else:
        print(-1)

else:
    b = [i for i in range(2**m) if i != k]
    ans = b + [k] + b[::-1] + [k]
    print(*ans)
