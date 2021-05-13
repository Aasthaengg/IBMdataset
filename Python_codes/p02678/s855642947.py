N, M = map(int, input().split())

pairs = [[] for _ in range(N)]  # pairs[i]:i+1と直接つながっている部屋のリスト
for _ in range(M):
    input_list = list(map(int, input().split()))
    pairs[input_list[0] - 1].append(input_list[1] - 1)
    pairs[input_list[1] - 1].append(input_list[0] - 1)

ans = [0] * (N - 1)
n_ans = 0   # ansを埋めた回数 -> N-1になったら終了
done = [True] + [False] * (N - 1) # 探索済リスト
todo = [0]

while n_ans < N - 1:
    for n in todo:
        for m in pairs[n]:
            if not done[m]:
                done[m] = True
                ans[m - 1] = n + 1
                n_ans += 1
                todo.append(m)

print('Yes')
print(*ans, sep='\n')