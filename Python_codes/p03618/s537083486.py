from collections import Counter
A = input()
N = len(A)
counter = Counter(A)
ans = N*(N-1)//2 + 1
for k,v in counter.items():
    if v==1:
        continue
    ans -= v*(v-1)//2
print(ans)