N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A.sort()
# B.sort()

if sum(A) < sum(B):
    print(-1)
else:
    # 方針
    # 不足している準備度を計算
    # 余っている準備度を大きなものから順に奪っていく

    T = []
    for i in range(N):
        T.append([A[i], B[i], A[i]-B[i]])

    T.sort(key=lambda x: x[2])

    if T[0][2] >= 0:
        print(0)
    else:
        fusoku = 0
        cnt = 0

        for ti in T:
            if ti[2] < 0:
                cnt += 1
                fusoku += abs(ti[2])

        T.sort(reverse=True, key=lambda x:x[2])
        for ti in T:
            fusoku -= ti[2]
            cnt += 1
            if fusoku <= 0:
                break

        print(cnt)
        
        
