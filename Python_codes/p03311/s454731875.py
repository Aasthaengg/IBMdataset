N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(N):
    B.append(A[i]-(i+1))

B.sort()
if (N % 2 == 1):
    b = B[N//2]
else:
    b = round((B[N//2]+B[N//2-1])/2)

ans = 0
for i in range(N):
    ans += abs(B[i] - b)

print(ans) 