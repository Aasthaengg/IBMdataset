N,K = (int(T) for T in input().split())
L = sorted([int(T) for T in input().split()],reverse=True)
print(sum(L[:K]))