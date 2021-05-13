import sys
N = int(input())
pre_a = int(input())
if pre_a != 0:
    print(-1)
    sys.exit()
ans = 0
for i in range(N-1):
    ai = int(input())
    if ai - pre_a < 1:
        ans += ai
    elif ai - pre_a == 1:
        ans += 1
    else:
        ans = -1
        break
    pre_a = ai

print(ans)