N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
cnt= float("inf")
for i in range(0,N):
    if abs(A-(T-H[i]*0.006)) < cnt:
        cnt = abs(A-(T-H[i]*0.006))
        ans = i+1
print(ans)