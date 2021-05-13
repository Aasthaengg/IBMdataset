N = int(input())
H = list(map(int, input().split()))
# H[N-2],H[N-3],...,H[0]について
for i in range(N - 2, -1, -1):
    if H[i] > H[i + 1] + 1:
        print("No")
        exit()
    if H[i] == H[i + 1] + 1:
        H[i] -= 1
print("Yes")
