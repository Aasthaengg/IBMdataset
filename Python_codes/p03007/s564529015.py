N = int(input())
A = sorted(list(map(int,input().split())))

ans_list = []
p = []
n = []

# 最大にプラス、最小にマイナスを割り当てる
p.append(A[-1])
n.append(A[0])

# 正ならプラスを負ならマイナスを割り当てる
for a in A[1:-1]:
    if a >= 0:
        p.append(a)
    elif a < 0:
        n.append(a)

# プラスが１つになるまで消す
res = n[0]
for ep in p[1:]:
    ans_list.append((res, ep))
    res -= ep
n[0] = res
p = [p[0]]

# マイナスがなくなるまで消す
res = p[0]
for en in n:
    ans_list.append((res, en))
    res -= en

# 残ったものが最大値
M = res
print(M)
for x, y in ans_list:
    print(x, y)