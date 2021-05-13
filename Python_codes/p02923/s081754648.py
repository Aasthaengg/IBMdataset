N = int(input())
H = list(map(int, input().split()))
maxi = 0
cnt = 0
for i in range(1, N):
    if H[i] <= H[i-1]:
        cnt += 1
    else:
        cnt = 0
    maxi = max(cnt, maxi)
print(maxi)