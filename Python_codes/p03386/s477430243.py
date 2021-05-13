A, B, K = map(int, input().split())

L = list(range(A, min(B, A+K))) + list(range(max(A, B-K+1), B+1))
L_no_duplication = set(L)
print(*sorted(L_no_duplication), sep="\n")