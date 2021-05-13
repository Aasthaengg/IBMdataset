
N, K = map(int, input().split())

if 2*N<=K and K<=4*N:
    if K%2==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")