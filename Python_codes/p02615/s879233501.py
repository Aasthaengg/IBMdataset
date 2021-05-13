
N = int(input())
X = list(map(int, input().split()))

X.sort(reverse=True)
ans = 0
cnt = 0
j = 0
for i in range(N):
    if i == 0:
        continue
    elif i == 1:
        ans += X[j]
        j += 1
    else:
        ans += X[j]
        cnt += 1
        if cnt == 2:
            j += 1
            cnt = 0

print(ans)
