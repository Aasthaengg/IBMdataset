n = int(input())
S = [int(t) for t in input().split()]
q = int(input())
T = [int(t) for t in input().split()]
assert n == len(S) and q == len(T)

print(sum(1 for t in T if t in S))
