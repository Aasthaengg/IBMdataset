from itertools import permutations
n = int(input())
p = tuple(input().split())
q = tuple(input().split())

# print(p)
# print(q)

l = [str(i+1) for i in range(n)]

cnt = 1
for v in permutations(l,n):
    if p == v:
        a = cnt
    if q == v:
        b = cnt
    cnt += 1
print(abs(a-b))