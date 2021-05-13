from collections import defaultdict
s = input()
n = len(s)

cnt = defaultdict(int)
for x in s:
    cnt[x] += 1

can_p = n//2
print(can_p-cnt['p'])
