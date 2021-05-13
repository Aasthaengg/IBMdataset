N,x = map(int, input().split())
*A, = map(int, input().split())

#貪欲法
ans = 0
for i in range(N-1):
    if (A[i]+A[i+1])<=x:
        continue
    #xより大きい分だけ食べる
    eat = (A[i]+A[i+1])-x
    if eat<=A[i+1]:
        A[i+1] -= eat
    else:
        A[i+1] = 0
        A[i] = A[i]-(eat-A[i+1])
    ans = ans + eat
print(ans)