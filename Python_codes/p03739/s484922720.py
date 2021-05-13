n = int(input())
a = list(map(int,input().split()))
ans1 = 0
num = 0
f1 = 1
for i in range(n):
    num += a[i]
    if f1:
        if num <=0:
            ans1 += 1-num
            num = 1
        f1 = 0
    else:
        if num >= 0:
            ans1 += num+1
            num = -1
        f1 = 1
ans2 = 0
num = 0
f1 = 0
for i in range(n):
    num += a[i]
    if f1:
        if num <=0:
            ans2 += 1-num
            num = 1
        f1 = 0
    else:
        if num >= 0:
            ans2 += num+1
            num = -1
        f1 = 1
print(min(ans1,ans2))