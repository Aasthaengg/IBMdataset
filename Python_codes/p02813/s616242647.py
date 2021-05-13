N = int(input())
P = int(''.join(input().split()))
Q = int(''.join(input().split()))
import itertools

perm = []
for num in itertools.permutations(list(range(1,N+1)),N):
    num = [str(n) for n in num]
    num = int(''.join(num))
    perm.append(num)
perm.sort()
p_ind = perm.index(P)
q_ind = perm.index(Q)

print(abs(p_ind-q_ind))



