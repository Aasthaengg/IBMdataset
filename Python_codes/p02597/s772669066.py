N = int(input())
C = input()
num_w = 0
num_r = 0
for i in range(N):
    if C[i] == 'R':
        num_r += 1
ans = 10**10
for i in range(N+1):
    if i == 0:
        ans = min(ans, num_r)
    elif i == N:
        ans = min(ans, num_w)
    else:
        if C[i-1] == 'W':
            num_w += 1
        else:
            num_r -=1 
        ans = min(ans, max(num_r, num_w))
print(ans)