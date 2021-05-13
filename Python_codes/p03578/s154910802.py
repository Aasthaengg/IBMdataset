from collections import Counter
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
dd = Counter(d)
tt = Counter(t)
# print(dd, tt)
ok = True
for i, j in tt.items():
    if i in dd:
        # print('Y')
        if dd[i] < j:
            ok = False
    else:
        ok = False
    # print(i, j, ok)

if ok:
    print('YES')
else:
    print('NO')