n,k = map(int,input().split())
L = list(map(int,input().split()))
L.sort()

sum1 = 0
cnt = 0
if k < L[0]:
    print(0)
    exit()
for i in range(n):
    sum1 +=L[i]
    if sum1 <=k:
        cnt +=1
        if i == n-1 and sum1 != k:
            cnt -=1
    else:
        break
print(cnt)