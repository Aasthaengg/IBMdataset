N = int(input())
B = input().split()
for i in range(N-1):
    B[i]=int(B[i])
ans = 0
for i in range(1,N-1):
    ans+=min(B[i-1],B[i])
ans += B[N-2]
ans += B[0]
print(ans)