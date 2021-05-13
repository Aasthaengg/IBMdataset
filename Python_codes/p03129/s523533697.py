N,K = [int(i) for i in input().split()]
if N % 2 == 0:
    if (N//2) >= K:
        print('YES')
        exit()
    else:
        print("NO")
        exit()
else:
    if (N+1)//2 >= K:
        print("YES")
    else:
        print("NO")