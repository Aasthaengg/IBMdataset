mod = 10 ** 9 + 7
cnt = [0] * 3
N = int(input())
A = list(map(int,input().split()))

ans = 1
for i in range(N):
    ans *= cnt.count(A[i])
    ans %= mod
    if ans == 0:
        break
    cnt[cnt.index(A[i])] += 1

print(ans)