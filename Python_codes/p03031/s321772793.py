n, m = map(int, input().split())
switches = [list(map(int, input().split())) for _ in range(m)]
correct = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    # pattern
    flg = True
    for p in range(m):
        cnt = 0
        for j in range(n):
            # 右シフト
            if (i >> j) & 1:
                if (j + 1) in switches[p][1:]:
                    cnt += 1
        if cnt % 2 != correct[p]:
            flg = False
            break
    if flg:
        ans += 1

print(ans)
