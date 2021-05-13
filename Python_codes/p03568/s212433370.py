import itertools
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in itertools.product((-1,0,1), repeat=N):
    for j in range(N):
        if (A[j]+i[j])%2==0:
            ans += 1
            break
print(ans)
