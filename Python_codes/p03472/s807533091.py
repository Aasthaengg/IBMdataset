import math
n, h = map(int, input().split())

atk = []
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    atk.append((a, 0))
    atk.append((b, 1))

atk.sort(key=lambda x: x[0], reverse=True)

# 通常の思考回路だと初めに何度か切り付けてそのあとに投げつけるが、初めに投げておいて繰り返すという逆の視点を持つ
max_blade = 0
for blade in atk:
    if blade[1] == 0:
        max_blade = max(max_blade, blade[0])
        break
    else:
        h = max(0, h - blade[0])
        ans += 1
        if h <= 0:
            break

if (h <= 0):
    print(ans)
else:
    print(math.ceil(h / max_blade) + ans)
