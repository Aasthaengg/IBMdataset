n = int(input())
a = list(map(int, input().split()))
accu = [0]*3
ans = 1
mod = 10**9+7
for i in a:
    cnt = 0
    for j in range(3):
        if i==accu[j]:
            cnt += 1
            idx = j
    if cnt==0:
        print(0)
        exit(0)
    ans *= cnt
    ans %= mod
    accu[idx] += 1
print(ans)