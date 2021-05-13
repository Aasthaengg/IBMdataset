from collections import Counter
n = int(input())
s = [input() for i in range(n)]
num = Counter(s)
mx = max(num.values())
T = []
for n in sorted(num):
    if num[n] == mx:
        print(n)