from collections import Counter
n = int(input())
A = Counter(list(map(int, input().split())))
ans = [0] * n
for x,y in A.items():
    ans[x-1] = y
for i in ans: print(i)