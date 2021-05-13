N = int(input())
A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))
ans = 0
for i in range(N):
    S = sum(A_1[0:i+1]) + sum(A_2[i:N])
    if S > ans:
        ans = S
 
print(ans)