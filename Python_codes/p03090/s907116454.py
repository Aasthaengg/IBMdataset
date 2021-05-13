from itertools import combinations as comb

N = int(input())
n = N-1 if N%2 else N
s = set()

for i in range(1, N+1):
    if N%2:
        a, b = i, N-i
    else:
        a, b = i, N-i+1
    if a<b:
        s.add((a, b))

l = [i for i in comb(range(1, N+1), 2) if not i in s]
print(len(l))
for i in l:
    print(*i)