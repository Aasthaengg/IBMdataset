[N,K] = list(map(int,input().split()))
h = []
for i in range(N):
    h.append(int(input()))

h.sort(reverse=True) 

out = 10**9

L = 0
R = K-1
while R<=N-1:
    D = h[L]-h[R]
    if out > D:
        out = D
    L+=1
    R+=1
print(out)