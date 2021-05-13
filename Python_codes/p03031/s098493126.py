N, M = map(int, input().split())

s = []
for i in range(M):
    i = list(map(int, input().split()))
    s.append(i[1:])

p = list(map(int, input().split()))

ans = 0
# i=0,1,2,...,2**N-1
# 全てのスイッチの場合の数
for i in range(2**N):
    flag = True

    # 各条件について
    for j in range(len(s)):
        # sのうち、ONになっているスイッチの数
        cnt = 0
        # 各スイッチについて
        for k in range(N):
            # そのスイッチがsに含まれる　かつ　ONになっている場合
            if (k + 1) in s[j] and ((i >> k) & 1):
                cnt += 1
        # 一つでも条件を満たさなかった時点でそのiで全点灯は不可能
        if cnt % 2 != p[j]:
            flag = False
            break

    if flag:
        ans += 1

print(ans)
