N=int(input())
A = [list(map(int, input().split())) for i in range(N)]
result=0
flag=True
isbreak=False
for m in range(N-1):
    for n in range(m+1,N):
        list_t=list(range(N))
        list_t.remove(m)
        list_t.remove(n)
        for t in list_t:
            if A[m][n]>A[m][t]+A[t][n]:
                result=-1                
                isbreak=True
                break
            elif A[m][n]==A[m][t]+A[t][n] and result!=-1:
                flag=False
                break
        if flag and result!=-1:
            result+=A[m][n]
        else:
            flag=True
        if isbreak:
            break
    if isbreak:
        break
print(result)
