N = int(input())
H = list(map(int, input().split()))
H.reverse()

ans = True
for i in range(len(H) - 1):
    if H[i] + 1 == H[i + 1]:
        H[i + 1] -= 1
    if H[i] + 1 < H[i + 1]:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
