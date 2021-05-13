N, M, K=map(int, input().split())

flg=False
for x in range(N+1):
    for y in range(M+1):
        temp = (N-x)*(M-y) + (x*y)
        if K==temp:
            flg=True
            break
if flg:
    print("Yes")
else:
    print("No")