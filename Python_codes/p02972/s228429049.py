N = int(input())
A = list(map(int,input().split()))

ans = [0 for i in range(N)]
for i in range(N-1,-1,-1):
    val = i+1
    if val*2>N:
        if A[i]==0:
            ans[i] = 0
        else:
            ans[i] = 1
    else:
        tmp = 0
        res = val
        while(1):
            if val>N:
                break
            tmp += ans[val-1]
            val += res

        if A[i]==0:
            if tmp%2==0:
                ans[i]=0
            else:
                ans[i]=1
        else:
            if tmp%2==0:
                ans[i]=1
            else:
                ans[i]=0
#print(*ans)
cnt = 0
b=[]
for i in range(N):
    if ans[i]==0:
        continue
    cnt += 1
    b.append(i+1)

print(cnt)
print(*b)
