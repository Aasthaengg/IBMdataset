N = int(input())
P = []
for _ in range(N):
    P.append(int(input()))
P.sort()
print(sum(P[:-1])+P[-1]//2)