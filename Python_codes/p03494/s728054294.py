N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans_sub = 0
    while A[i]%2 == 0:
        A[i]/=2
        ans_sub += 1
    
    if i == 0:
        ans = ans_sub
    else:
        ans = min(ans_sub, ans)

print(ans)