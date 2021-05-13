N = int(input())
arr = list(map(int, input().split()))
ans = [0]*N
for i in range(N):
    target = N-1-i
    tmp = 0
    for k in range(target,N,target+1):
        tmp += ans[k]
    if tmp % 2 == arr[target]:
        ans[target] = 0
    else:
        ans[target] = 1
ans2 = []
for i in range(N):
    if ans[i] == 1:
        ans2.append(i+1)
print(len(ans2))
print(*ans2)