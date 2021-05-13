s = input()

cnt = [0]*26
for c in s:
    cnt[ord(c) - ord('A')] += 1

if cnt.count(2) == 2:
    print('Yes')
else:
    print('No')
