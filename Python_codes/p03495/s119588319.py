import sys
import collections

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
li = []
ans = 0

B = set(A)

cnt = len(B)

#for x in B:
#    a = A.count(x)
#    li.append(a)

li = list(collections.Counter(A).values())
li = sorted(li)

if cnt - K > 0:
    for x in range(cnt - K):
        ans += li[x]
    print(ans)

else :
    print(ans)