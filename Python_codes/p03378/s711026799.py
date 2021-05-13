N, M, X = map(int, input().split())
A = list(map(int, input().split()))

l = list(range(1, X))
r = list(range(X+1, N+1))

l_c = len(set(A)&set(l))
l_r = len(set(A)&set(r))

print(min(l_c, l_r))