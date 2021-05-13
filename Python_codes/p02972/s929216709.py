N = int(input())
A = [0]
A += list(map(int,input().split()))
Res = [0] * (N+1)

for i in range(N):
    Res[N-i] = A[N-i] ^ (sum(Res[::N-i]) % 2)

print(sum(Res))
ResN = []
for i,r in enumerate(Res):
    if i==0:
        continue
    if r == 1:
        ResN.append(str(i))

if ResN:
    print(' '.join(ResN)) # ここの空白を忘れてはならない

