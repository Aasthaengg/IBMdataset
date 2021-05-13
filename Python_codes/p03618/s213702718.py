from collections import defaultdict
A = input()
N = len(A)
cnt = defaultdict(int)
for k in A:
    cnt[k] += 1
print(1+N*(N+1)//2-sum([cnt[k]*(cnt[k]+1)//2 for k in cnt]))