N, K = map(int, input().split())  # N個の寿司からK個
sushi = []
for i in range(N):
    t, d = map(int, input().split())  # 寿司の種類, 寿司の美味しさ
    sushi.append([t, d])

sushi.sort(key=lambda x: x[1], reverse=True)  # 美味しさで降順ソート
kind = set()
stack = []
ans = 0
for t, d in sushi[:K]:
    if t in kind:
        stack.append(d)
    else:
        kind.add(t)
    ans += d

ans += len(kind)**2
point = ans
for t, d in sushi[K:]:
    if len(stack) == 0:  # K個の寿司全てが1つずつしか存在しないなら交換しようがない
        break

    # 交換を行う
    if t in kind:
        continue
    else:
        point -= stack.pop()
        point += d
        point += 2*len(kind) + 1  # 平方の数列の階差
        kind.add(t)
    ans = max(ans, point)
print(ans)
