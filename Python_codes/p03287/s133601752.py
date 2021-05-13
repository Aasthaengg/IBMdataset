from itertools import accumulate
N,M = map(int,input().split())
A = list(map(int,input().split()))
As = [0]
for i in accumulate(A):
    As.append(i%M)
count = {}
ans = 0
for i in As:
    if i not in count:
        count[i] = 1
    else:
        ans += count[i]
        count[i] += 1
print(ans)