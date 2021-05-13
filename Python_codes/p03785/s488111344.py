#54 A - Airport Bus
N,C,K = map(int,input().split())
T = [int(input()) for _ in range(N)]
T = sorted(T,reverse = False)
# 最後の一人をカウントするための番兵
T.append(10**10)

ans = 0
bus = 1
first = T[0]
for i in range(1,N+1):
    # T[i] がバスに乗ることができるとき
    if (bus < C) and (T[i] <= first + K):
        bus += 1
    # T[i] がバスに乗ることができないとき
    else:
        # 新しいバスの first になる
        ans += 1
        bus = 1
        first = T[i]
        
print(ans)
