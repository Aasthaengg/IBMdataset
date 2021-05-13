N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

from collections import Counter
D.sort()
d = Counter(D)
T.sort()
t = Counter(T)

answer = 'YES'

for i in range(M):
    if t[T[i]] > d[T[i]]:
        answer = 'NO'
        break
        
print(answer)