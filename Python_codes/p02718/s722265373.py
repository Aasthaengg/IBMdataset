ri = lambda S: [int(v) for v in S.split()]
N, M = ri(input())
A = ri(input())
T = sum(A)
thresh = (1/(4*M)) * T
c = len([v for v in A if v >= thresh])
print("Yes" if c >= M else "No")

