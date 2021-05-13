N = int(input())
H = list(map(int, input().split()))

if N == 1:
    print("Yes")
else:
    for i in range(N):
        if i == 0:
            H[i] -= 1
        else:
            if H[i] > H[i - 1]:
                H[i] -= 1
            elif H[i] < H[i - 1]:
                print("No")
                break
    else:
        print("Yes")