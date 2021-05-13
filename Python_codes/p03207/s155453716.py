N = int(input())
P = []
for _ in range(N):
    P.append(int(input()))

print(sum(P)-max(P)+(max(P)//2))
