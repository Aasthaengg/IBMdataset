n, q = [int(i) for i in input().split()]
que = []
ans_count = 0 #出力数
time = 0 #経過時間
# data読み込み
for i in range(n):
    que.append([i for i in input().split()])

while(ans_count!=n):
    pop_process = que.pop(0)
    pop_process[1] = int(pop_process[1])
    # 末尾から追加、先頭から取り出す
    if pop_process[1] <= q:
        time += pop_process[1]
        print('{0} {1}'.format(pop_process[0], time))
        ans_count += 1
    else:
        time += q
        pop_process[1] -= q
        que.append(pop_process)
