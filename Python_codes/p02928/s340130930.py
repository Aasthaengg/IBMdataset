n,k = map(int,input().split())
A=list(map(int, input().split()))
mod = 10**9+7
ans_inlist = [0]*n
ans_forwardlist = [0]*n
for i in range(n):
    for j in range(n):
        if A[i]>A[j]:
            ans_forwardlist[j] += 1
            if i<j:
                ans_inlist[j]+=1
#print(sum(ans_forwardlist), sum(ans_inlist))
ans = (k*(k-1)//2)*sum(ans_forwardlist)%mod +k*sum(ans_inlist)%mod
print(ans%mod)

