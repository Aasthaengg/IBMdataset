N = int(input())
A = list(map(int,input().split()))
cur = 0
cnt = 0
cum = A[0]
for i in range(1,N):
    if A[i]&cum==0:
        cum = cum^A[i]
    else:
        cnt += i-cur
        cum = cum^A[cur]
        cur += 1
        while cur<i:
            if cum&A[i]==0:break
            else:
                cnt += i-cur
                cum = cum^A[cur]
                cur += 1
        cum = cum^A[i]
cnt += ((N-cur)*(N-cur+1))//2
print(cnt)