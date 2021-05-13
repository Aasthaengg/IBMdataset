N = int(input())
h = list(map(int,input().split()))
ans = 0
for i in range(N):
    while(h[i] != 0):
        ans += 1
        for j in range(i, N):
            if h[j] >= 1:  h[j] -= 1
            else:  break
print(ans)