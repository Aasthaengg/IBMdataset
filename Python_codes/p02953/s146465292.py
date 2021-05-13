def resolve():
    N = int(input())
    H = list(map(int, input().split()))
    flag = 0
    for i in range(1, N):
        if H[i*-1-1] > H[i*-1]:
            if H[i*-1-1]-1 == H[i*-1]:
                H[i*-1-1] -= 1
            else:
                flag = 1
    print("Yes" if flag==0 else "No")
resolve()