N = int(input())
A = list(map(int,input().split()))
ans = 0
now = 1
while now < N:
    if A[now] == A[now-1]:
        ans += 1
        now += 2
    else:
        now += 1
print(ans)