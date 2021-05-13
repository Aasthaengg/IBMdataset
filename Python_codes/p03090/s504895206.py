from itertools import combinations as comb

N = int(input())
n = N-1 if N%2 else N
m = N if N%2 else N+1
s = {(i, n+1-i) for i in range(1, N+1) if i<n+1-i}

l = [i for i in comb(range(1, N+1), 2) if not i in s]
print(len(l))
for i in l:
    print(*i)