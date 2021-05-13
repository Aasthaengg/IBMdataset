import re
import sys
s = re.findall('[a-z]', sys.stdin.read().lower())
letters = 'abcdefghijklmnopqrstuvwxyz'
cnt = [0]*26
for i in s:
    point = 0
    for j in letters:
        if i == j:
            cnt[point] += 1
            break
        point += 1
for i in range(26):
    print('%s : %d'%(letters[i], cnt[i]))
