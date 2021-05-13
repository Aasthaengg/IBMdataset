# C - Fennec vs Monster
N,K = map(int,input().split())
H = list(map(int,input().split()))
H = sorted(H)
print(sum(H[:max(0,N-K)]))