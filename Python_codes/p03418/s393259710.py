n,k = map(int,input().split())
count = 0
flag = False
if k==0:
    flag = True
for i in range(k+1,n+1):
    if n%i >= k:
        count += (i-k)*(n//i) + n%i - k + 1
    else:
        count += (i-k)*(n//i)
if flag:
    print(n*n)
else:
    print(count)