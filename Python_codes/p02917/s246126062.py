N = int(input())
B = [int(i) for i in input().split()]

ans = 0
ans += B[0]
for i in range(1, N-1):
    syou = min(B[i-1], B[i])
    ans+=syou
ans+=B[N-2]
print(ans)