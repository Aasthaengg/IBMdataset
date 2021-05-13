from collections import Counter
n = int(input())
A = Counter([int(input()) for _ in range(n)])
cnt = 0
for k in A.values():
    if k%2 != 0:
        cnt +=1
print(cnt)