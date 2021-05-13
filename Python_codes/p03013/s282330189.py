N, M = map(int,input().split())
A_list = set([int(input()) for _ in range(M)])
Dp_list = [0] * (N+1)
Dp_list[0] = 1

if 1 in A_list:
    Dp_list[1] = 0
else:
    Dp_list[1] = 1

if N != 1:
    for i in range(2, N + 1):
        if i in A_list:
            continue

        Dp_list[i] = Dp_list[i-2] + Dp_list[i-1]
        Dp_list[i] %= 1000000007
    print(Dp_list[N])
else:
    print(1)