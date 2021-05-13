from collections import Counter
N = int(input())
A = list(map(int, input().split()))

ans = 0
counter = Counter(A)
keys = sorted(counter.keys(), reverse=True)
flag = False
for k in keys:
    if ans == 0 and counter[k] >= 4:
        ans = k*k
        flag = True
        break
    elif ans == 0 and counter[k] >= 2:
        ans = k
    elif ans != k and counter[k] >= 2:
        ans = ans * k
        flag = True
        break
if flag:
    print(ans)
else:
    print(0)