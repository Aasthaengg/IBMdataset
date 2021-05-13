N = int(input())
a = list(map(int, input().split()))
ave_a = sum(a)/N
cnt = 101
ans = 0

for i in range(N):
    tmp = abs(ave_a-a[i])
    if(tmp < cnt):
        cnt = tmp
        ans = i
print(ans)