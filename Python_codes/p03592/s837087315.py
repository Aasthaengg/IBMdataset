def func():
    global n,m,k
    for i in range(n+1):
        for j in range(m+1):
            tmp = i*m + j*n -(j*i)*2
            if tmp == k:
                return "Yes"
    return "No"
n,m,k = map(int,input().split())
ans = func()
print(ans)
