from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
cnt = defaultdict(int)

for i in range(n):
    cnt[a[i]] += 1
flag = True

if 0 in cnt.keys():
    del cnt[0]

for i in range(n - 1, 0, -2):
    if cnt[i] != 2:
        flag = False
        break 
print((2 ** (n // 2)) % (10 ** 9 + 7) if flag else 0)