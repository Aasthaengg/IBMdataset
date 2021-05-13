N,D,A = map(int,input().split())

XH = sorted(tuple(map(int,input().split())) for _ in range(N))

X = [x for x,h in XH]
H = [h for x,h in XH]

dH = [0]*(N+1)

cnt = 0
acc = 0

cnt = 0
i = 0
j = 0
while i < N:
    while j < N and X[j] <= X[i]+2*D:
        j += 1

    acc -= dH[i]
    H[i] -= acc
    if H[i] > 0:
        c = (H[i]-1)//A + 1
        acc += c*A
        dH[j] += c*A
        cnt += c
    i += 1

print(cnt)