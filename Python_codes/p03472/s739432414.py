N, H = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort(reverse=True)
B.sort(reverse=True)

"""
a_max, a_max, ..., a_max, b, b, ..., b　となる

a_maxより強いbは強い順に投げておいて、まだ倒せなかったらa_maxを振ると考える
実際には計算された回数だけa_maxを振り、その後bを投げれば良い
"""

cnt = 0
a_max = max(A)

for b in B:
    if b < a_max:
        break
    H -= b
    cnt += 1
    if H <= 0:
        break

if H > 0:
    if H % a_max == 0:
        cnt += H // a_max
    else:
        cnt += H // a_max + 1

print(cnt)
