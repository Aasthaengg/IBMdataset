N = int(input())
arr = list(map(int, input().split()))
if N == 0:
    print(1 if arr[0]==1 else -1)
    exit()
elif arr[0] != 0:
    print(-1)
    exit()
sum_arr = [arr[-1]]*N
for i in range(1,N):
    sum_arr[i] = sum_arr[i-1]+arr[N-i]
sum_arr = sum_arr[::-1]
ans = [1]*(N+1)
for i in range(1,N+1):
    if ans[i-1]-arr[i-1] < 0:
        print(-1)
        exit()
    tmp = min((ans[i-1]-arr[i-1])*2,sum_arr[i-1])
    ans[i] = tmp
for i in range(min(25,N+1)):
    if ans[i] > 2**i:
        print(-1)
        exit()
if ans[N] != arr[-1]:
    print(-1)
    exit()
print(sum(ans))