(N, M), *AB = [list(map(int, s.split())) for s in open(0)]
A = sorted(AB[0])
D = []
for b, c in sorted(AB[1:], key=lambda x: (-x[1], x[0])):
    D.extend([c] * b)
    if len(D) >= N:
        D = D[:N]
        break
D = D[::-1]
for i in range(N):
    if not D or D[-1] <= A[i]:
        break
    A[i] = D.pop()

print(sum(A))