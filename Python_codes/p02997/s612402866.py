N, K = (int(i) for i in input().split())

#最大化すると(N-2)*(N-1)//2組
ma = (N-2)*(N-1)//2
cou = 0
if N == 2:
    if K > 0:
        print("-1")
    else:
        print("1")
        print("1 2")
else:
    if K > ma:
        print("-1")
    else:
        print(N-1 + ma - K)
        for i in range(1, N):
            print("{} {}".format(i, N))
        for i in range(1, N):
            for j in range(1, N):
                if cou >= ma - K:
                    exit()
                if i < j:
                    print(i, j)
                    cou += 1