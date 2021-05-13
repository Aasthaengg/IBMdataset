n,m,d = list(map(int, input().split()))
if d==0:
    res = (m-1)/n
else:
    res = (2*(m-1)*(n-d))/(n*n)
print(res)
