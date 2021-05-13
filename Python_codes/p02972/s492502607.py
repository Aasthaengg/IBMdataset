from sys import exit
from collections import defaultdict as dd
n = int(input())
A = list(map(int, input().split()))

dic = dd(int)
for i, a in enumerate(A):
    dic[i+1] = a

baisu = dd(set)
for num in range(1, n+1):
    for i in range(1, n+1):
        if num * i > n:
            break
        baisu[num * i].add(num)
#print(baisu)

box = dd(int)

#dic -> baisu -> box
for num in range(n, 0, -1):
    kosu = dic[num]
    for yakusu in list(baisu[num]):
        dic[yakusu] += kosu
        dic[yakusu] %= 2
        box[num] += kosu

ans = []
for i in range(1, n+1):
    if box[i] >= 1:
        ans.append(i)
print(sum([i > 0 for i in ans]))
print(*ans, sep=" ")