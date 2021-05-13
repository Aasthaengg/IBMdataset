# ベクトルを固定して全探索まではわかる 実装がわからん
# いやべつに順番は関係ないのか？ 「残っているボールを 1つ選んで回収する。」

n = int(input())
if n == 1:
    print(1)  # 「ただし、1つ目に選んだボールについては必ずコスト 1かかる。」
    exit()
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

ans = 10**18
for p in range(n):
    for q in range(n):
        if p == q:
            continue
        vector = [points[p][0] - points[q][0], points[p][1] - points[q][1]]
        tmp = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if points[i][0] - points[j][0] == vector[
                        0] and points[i][1] - points[j][1] == vector[1]:
                    tmp += 1

        ans = min(ans, n - tmp)

print(ans)