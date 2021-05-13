N = int(input())
cmin = N
for i in range(1,N):
    j = N-i
    a = str(i)
    b = str(j)
    cnt = 0
    for k in range(len(a)):
        cnt += int(a[k])
    for k in range(len(b)):
        cnt += int(b[k])
    cmin = min(cmin,cnt)
print(cmin)