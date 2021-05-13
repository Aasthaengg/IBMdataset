N,K=list(map(int, input().split()))
P=list(map(int, input().split()))
P.sort()
L=P[:K]
print(sum(L))