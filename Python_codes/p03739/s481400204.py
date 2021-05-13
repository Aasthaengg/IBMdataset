n, *A = map(int, open(0).read().split())
def sgn(n):
    return 0 if n==0 else 1 if n>0 else -1

a = A[0]
C = [0 if a>0 else -a+1, 0 if a<0 else a+1]
S = [max(1, a), min(-1, a)]

for a in A[1:]:
    for i, s in enumerate(S):
        sgn_sum = sgn(s)
        if sgn(s+a) == -sgn_sum:
            S[i] += a
        else:
            C[i] += abs(s+a+sgn_sum)
            S[i] = -sgn_sum

print(min(C))