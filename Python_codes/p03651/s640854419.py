N, K = [int(i) for i in input().split()]
A = sorted([int(i) for i in input().split()], reverse=True)

for v in A:
    if K==v:
        print("POSSIBLE")
        quit()
if K > A[0]:
    print("IMPOSSIBLE")
    quit()

d = []
for i in range(N-1):
    d.append(A[i]-A[i+1])

for v in d:
    if v:
        K %= v

if K:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")