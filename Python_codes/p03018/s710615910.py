import re

S = 'S' + input()
new_s = list(S.replace('BC', 'D'))


cnt = 0
A = 0
for i in range(len(new_s)):
    if new_s[i] == 'A':
        A += 1
    elif new_s[i] == 'D':
        cnt += A
    else:
        A = 0
print(cnt)