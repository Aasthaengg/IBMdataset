from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)

cnt = 0
for v in c.values():
    cnt += v-1

ans = len(set(A))
if cnt % 2 != 0:
    ans -= 1
    
print(ans)