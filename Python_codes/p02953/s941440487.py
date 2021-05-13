N = int(input())
H = list(map(int, input().split()))

suc = "Yes"
maxN = H[0]
for i in range(N):
    if maxN - 1 > H[i]:
        suc = "No"
        break
    elif maxN < H[i]:
        maxN = H[i]
print(suc)

