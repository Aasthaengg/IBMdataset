from collections import Counter
s = input()
cnt = Counter(s)
n_p = cnt['p']
print(len(s) // 2 - n_p)