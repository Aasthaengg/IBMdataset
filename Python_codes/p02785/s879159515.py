N,K = map(int,input().split())
H = list(map(int,input().split()))

H = sorted(H)

if N < K:
    K = N

for i in range(K):
    del[H[-1]]

print(sum(H))