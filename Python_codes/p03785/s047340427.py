N,C,K = map(int,input().split())

T = []

for i in range(N):
    T.append(int(input()))
T.sort()
res = 0
cnt = 0
i = 0

while i < N:
    lim = T[i]+K
    while T[i] <= lim and cnt < C:
        i += 1
        cnt += 1
        if N == i:
            break
    res += 1
    cnt = 0
print(res)