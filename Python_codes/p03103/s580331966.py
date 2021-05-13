N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x:x[0])

cnt = 0
cost = 0
for a, b in AB:
    if M >= cnt:
        cnt += b
        cost += a*b
        if cnt == M:
            print(cost)
            break
        elif cnt > M:
            cost += (M-cnt)*a
            print(cost)
            break