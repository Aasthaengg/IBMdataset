N,K = input().split()
scores = [int(s) for s in input().split()]

N = int(N)
K = int(K)

for i in range(K,N):
    if scores[i] <= scores[i-K]:
        print("No")
    else:
        print("Yes")