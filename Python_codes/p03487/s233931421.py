from collections import Counter

N = int(input())
a = list(input().split())
seq = [int(a[i]) for i in range(N)]
Cons = Counter(seq)

num = list(Cons.items())
count = 0

for i in range(len(num)):
    dif = int(num[i][1]) - int(num[i][0])
    count += (dif if dif >= 0 else int(num[i][1]))

print(count)