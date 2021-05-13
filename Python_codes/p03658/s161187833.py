N,K = map(int,input().split())
L = [int(n) for n in input().split()]

print(sum(sorted(L)[N-K:]))