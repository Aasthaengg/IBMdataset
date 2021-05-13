n = int(input())
a = list(map(int, input().split()))
accu = 0
tmp = 0
for i in range(n):
    accu += a[i]
    if i%2==0:
        if accu<=0:
            tmp += 1-accu
            accu = 1
    else:
        if accu>=0:
            tmp += accu+1
            accu = -1
ans = tmp
accu = 0
tmp = 0
for i in range(n):
    accu += a[i]
    if i%2==1:
        if accu<=0:
            tmp += 1-accu
            accu = 1
    else:
        if accu>=0:
            tmp += accu+1
            accu = -1
ans = min(tmp, ans)
print(ans)