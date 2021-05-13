from collections import Counter
A = input()
N = len(A)
ans = 1 + N*(N-1)//2
count = Counter(A)
for k, v in count.items():
    ans -= v*(v-1)//2
print(ans)