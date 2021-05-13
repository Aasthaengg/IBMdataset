N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]
AB_soretd = sorted(AB, key=lambda a: a[0])
drink_cnt = 0
ans = 0
for i in range(N):
    a = AB_soretd[i][0]
    b = AB_soretd[i][1]
    if M > drink_cnt + b:
        ans += a * b
        drink_cnt += b
    else:
        for i in range(1,b+1):
            if M == drink_cnt + i:
                ans += a * i
                break
        break
print(ans)


