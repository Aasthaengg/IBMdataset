N = int(input())
cnt = 0
ans = "No"
for i in range(N):
    D = list(map(int, input().split()))
    if D[0] == D[1]:
        cnt += 1
        if cnt >= 3:
            ans = "Yes"
            continue
    else:
        cnt = 0
print(ans)
