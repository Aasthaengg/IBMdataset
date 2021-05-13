N = int(input())
A = list(map(int,input().split()))
color = [0,0,0]
ans = 1
for i in range(N):
    p = 0
    flag = 0
    for j in range(3):
        if A[i] == color[j]:
            p += 1
            if flag == 0:
                color[j] += 1
                flag = 1  
    ans *= p
    ans %= 10**9+7
print(ans)