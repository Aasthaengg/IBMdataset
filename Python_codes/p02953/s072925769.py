N = int(input())
H = list(map(int, input().split()))

base = H[0]

for i in range(1, N):
    if base < H[i]:
        base = H[i] - 1
    elif base > H[i]:
        print("No")
        exit(0)
    else:
        base = H[i]

print("Yes")