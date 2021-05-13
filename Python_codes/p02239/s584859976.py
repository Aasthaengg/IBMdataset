import collections

N = int(input())
M = []
for i in range(N):
    a = list(map(int,input().strip().split()))
    b = [int(i+1 in a[2:]) for i in range(N)]
    M.append(b)

D = [-1 for _ in range(N)]
D[0] = 0 # 始点への距離は 0, 他の距離は-1
Q = collections.deque()
Q.append(0) # 始点
while len(Q) > 0:
    #print("bfs", Q) # 各ステップでの Q の動作を確認
    cur = Q.popleft()
    for dst in range(N):
        # curからdstに移動可能かつ、dstが未訪問だったら
        if M[cur][dst] == 1 and D[dst] == -1:
            D[dst] = D[cur]+1
            Q.append(dst) # Qにdstを詰める
for v in range(N):
    print(v+1, D[v])

