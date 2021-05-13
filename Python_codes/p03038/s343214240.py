from operator import itemgetter

N,M = map(int,input().split())
A = list(map(int,input().split()))
BC = []
for i in range(M):
    B,C = map(int,input().split())
    BC.append([B,C])

BC.sort(key = itemgetter(1),reverse=True)

change = []
for b,c in BC:
    change += [c] * b
    if len(change) > N:
        break
A += change
A.sort(reverse=True)
answer = sum(A[:N])
print(answer)