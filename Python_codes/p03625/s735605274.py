from collections import Counter

n = int(input())
a = list(map(int, input().split()))
d = Counter(a)
ans = 0
j = False

for k, v in sorted(d.items(), key = lambda x: -x[0]):
    if v >= 4:
        if ans == 0:
            ans = k*k
            j = True
            break
        else:
            ans *= k
            j = True
            break
    elif v >= 2:
        if ans == 0:
            ans = k
        else:
            ans *= k
            j = True
            break
if j == True:
    print(ans)
else:
    print(0)