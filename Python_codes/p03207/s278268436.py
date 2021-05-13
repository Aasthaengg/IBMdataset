# B - Christmas Eve Eve

N = int(input())
P = []
for _ in range(N):
    P.append(int(input()))
    
P.sort(reverse=True)

print(P[0]//2 + sum(P[1:]))