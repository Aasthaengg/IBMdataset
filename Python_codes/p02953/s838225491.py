N = int(input())
H = list(map(int, input().split()))
H[0] -= 1
ans = "Yes"
for i in range(1, N):
    if H[i-1] == H[i]:
        continue
    elif H[i-1] <= H[i]-1:
        H[i] -= 1
    elif H[i-1] > H[i]:
        ans = "No"
        break

print(ans)
