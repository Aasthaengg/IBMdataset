from collections import Counter

s = str(input())

d = Counter(s)
l = [0] * 3
k = 0
for i, j in d.items():
    l[k] = j
    k += 1
Palindrome = False
for i in range(3):
    if abs(l[i-1] - l[i]) > 1:
        Palindrome = True

if Palindrome:
    print('NO')
else:
    print('YES')