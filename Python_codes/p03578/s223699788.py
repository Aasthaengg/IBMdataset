N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

cnt = {}
for d in D:
    if d not in cnt:
        cnt[d] = 1
    else:
        cnt[d] += 1
ans = True
for t in T:
    if t not in cnt:
        ans = False
        break
    elif cnt[t] == 0:
        ans = False
        break
    else:
        cnt[t] -= 1

if ans:
    print("YES")
else:
    print("NO")
