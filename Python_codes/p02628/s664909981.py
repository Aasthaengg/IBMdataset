N,K= map(int,input().split())
P = list(map(int,input().split()))
Pnew = sorted(P)
total = 0
for i in range(K):
    total += Pnew[i]

print(str(total))
