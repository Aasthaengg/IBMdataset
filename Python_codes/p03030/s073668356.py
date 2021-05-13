N = int(input())
A = []
for i in range(N):
    S, P = input().split()
    A.append((S,-int(P), i))
A.sort()
print(*list(i+1 for _, _, i in A))