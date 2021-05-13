from collections import Counter

n = int(input())
s = input()
counter = Counter(s)
ans = counter['R'] * counter['G'] * counter['B']
for i in range(n):
    for j in range(i, n):
        k = j + (j - i)
        if k >= n:
            break
        if s[i] != s[j] != s[k] != s[i]:
            ans -= 1

print(ans)