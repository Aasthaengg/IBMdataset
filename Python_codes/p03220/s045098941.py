N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))
best = 1000.0
point = 0
ans = 0
for i in range(N):
    ans = abs(A - (T - H[i]*0.006))
    if best > ans:
        best = ans
        point = i + 1
print(point)
