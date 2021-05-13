# 第6回 ドワンゴからの挑戦状 予選: A – Falling Asleep
N = int(input())
s, t = [], []
for _ in range(N):
    tmp = input().split()
    s.append(tmp[0])
    t.append(int(tmp[1]))
X = input()

idx = s.index(X)
print(sum(t[idx + 1:]))