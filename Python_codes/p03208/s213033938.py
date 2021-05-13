N,K = map(int,input().split())
T = [int(input()) for i in range(N)]

T.sort()
P = []
for i in range(N-K+1):
    P.append(T[i+K-1] - T[i])

print(min(P))