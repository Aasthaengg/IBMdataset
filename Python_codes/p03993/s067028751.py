N = int(input())
A = list(map(lambda x:int(x)-1,input().split()))
ans = 0
paired = []
flag = [0]*N
for i in range(N):
    if flag[i]:
        continue
    else:
        if A[A[i]] == i:
            ans += 1
            flag[A[i]] = 1
print(ans)