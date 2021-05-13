N = int(input())
P = [int(input()) for i in range(N)]
P.sort(reverse=True)
print(P[0]//2 + sum(P[1:]))