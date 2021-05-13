from collections import deque
N,D,A = map(int, input().split())
ps = []
def ceil(a,b):
    return -(-a//b)

for i in range(N):
    x,h = map(int, input().split())
    ps.append([x,h])

ps.sort()
damage = 0
cnt = 0
q = deque([])
for x,h in ps:
    while len(q) > 0 and q[0][0] < x:
        # 範囲外のものはダメージを与えられない
        _, d = q.popleft()
        damage -= d
    # 残りダメージ
    h_rest = h - damage
    if h_rest <= 0: continue
    num = ceil(h_rest, A)
    damage += num * A
    cnt += num
    r = x + 2*D
    q.append((r,num*A))
print(int(cnt))
