import sys
input = sys.stdin.buffer.readline
X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P = sorted(P, reverse=True)[:X]
Q = sorted(Q, reverse=True)[:Y]
Ans = []
for p in P:
    Ans.append((p, 1))
for q in Q:
    Ans.append((q, 2))
for r in R:
    Ans.append((r, 3))
Ans.sort(reverse=True)

x = 0
y = 0
num = 0
ans = 0

for i, j in Ans:
    if j == 1:
        if x == X:
            continue
        else:
            x += 1
            num += 1
            ans += i
    elif j == 2:
        if y == Y:
            continue
        else:
            y += 1
            num += 1
            ans += i
    else:
        num += 1
        ans += i
    if num == X+Y:
        break
print(ans)
