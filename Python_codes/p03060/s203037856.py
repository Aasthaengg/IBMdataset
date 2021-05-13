n = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

ans = 0
for i in range(n):
    if V[i] > C[i]:
        ans += V[i] - C[i]
        
print(ans)