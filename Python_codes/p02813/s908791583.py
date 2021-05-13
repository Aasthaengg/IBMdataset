n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
##print(P)
#print(Q)
import itertools
X = []
for p in itertools.permutations(range(1, n+1)):
    X.append(p)
#print(X)
for i in range(len(X)):
    if P == X[i]:
        a = i
        break
for i in range(len(X)):
    if Q == X[i]:
        b = i
        break
print(abs(a-b))
