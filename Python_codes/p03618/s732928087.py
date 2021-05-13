import collections

A = input()
c = collections.Counter(A)

ans = len(A)*(len(A)-1)//2+1

for v in c.values():
    if v >= 2:
        ans -= v*(v-1)//2

print(ans)
