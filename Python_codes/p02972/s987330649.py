N = int(input())
A = list(map(int,input().split()))
chk = [0] * N 
ans = []
cnt = 0

for i in reversed(range(1,N+1)):
    if i > N // 2:
        if A[i-1] == 1:
            ans.append(i)
            chk[i-1] = 1
            cnt += 1
    else:
        j = 2 * i
        ret = 0
        while j <= N:
            ret += chk[j-1] 
            j += i
        if A[i-1] != ret%2:
            ans.append(i)
            chk[i-1] = 1
            cnt += 1
            
print(cnt)
print(*ans)