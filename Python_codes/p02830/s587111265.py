N = int(input())
S,T = input().split()

A = []
for s, t in zip(S,T):
    A += s+t
print(*A, sep='')