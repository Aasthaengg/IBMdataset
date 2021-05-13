n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))

tc = []
ac = []

tc.append((t[0], t[0]))
flag = 1
for i in range(n-1):
    if t[i+1] > t[i]:
        tc.append((t[i+1], t[i+1]))
    elif t[i+1] < t[i]:
        flag = 0
    else:
        tc.append((1, t[i+1]))

a.reverse()
ac.append((a[-1], a[-1]))
for i in range(n-1):
    if a[i+1] > a[i]:
        ac.append((a[i+1], a[i+1]))
    elif a[i+1] < a[i]:
        flag = 0
    else:
        ac.append((1, a[i+1]))

ac.reverse()
import sys
if flag == 0:
    print(0)
    sys.exit()

else:
    ans = 1
    for i in range(n):
        maxi = min(tc[i][1], ac[i][1])
        mini = max(tc[i][0], ac[i][0])
        ans *= max(0, maxi-mini+1)
        ans %= 10**9+7

    print(ans)
