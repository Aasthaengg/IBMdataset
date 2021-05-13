N = int(input())
A = list(map(int, input().split()))
MAX = 10**18
A.sort()
ans = 1
for i in range(len(A)):
    ans = ans * A[i]
    if ans > MAX:
        print(-1)
        exit()
print(ans)

