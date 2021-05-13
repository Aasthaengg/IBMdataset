from collections import defaultdict
S = list(input())
T = list(input())

Ms = defaultdict(int)
Mt = defaultdict(int)

for i in range(len(S)):
    Ms[S[i]] += 1
    Mt[T[i]] += 1

ans = "Yes"

A = list(Ms.values())
A.sort()
B = list(Mt.values())
B.sort()

for i in range(len(A)):
    if A[i] != B[i]:
        ans = "No"
        break

print(ans)
