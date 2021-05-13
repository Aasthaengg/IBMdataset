N = int(input())
P = []
for i in range(N):
    P.append(int(input()))
print(int(sum(P)-max(P)/2))
