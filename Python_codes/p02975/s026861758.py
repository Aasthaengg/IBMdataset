from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
if set(a) == {0}:
    print('Yes')
    exit()

flag = 0
if n % 3 == 0:
    if len(cnt) == 2:
        if cnt.get(0) == n // 3:flag = 1
    elif len(cnt) == 3:
        if len(set(cnt.values())) == 1:
            new_a = list(cnt.keys())
            if new_a[0]^new_a[1] == new_a[2]:flag = 1

print('Yes' if flag else 'No')