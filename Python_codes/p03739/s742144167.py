n = int(input())
a = list(map(int,input().split()))

ans = 0
f = 1
num = 0
for i in range(n):
    num += a[i]
    if f:
        if num <= 0:
            ans += 1 - num
            num = 1
        f = 0
    else:
        if num >= 0:
            ans += abs(-1 - num)
            num = -1
        f = 1

ans_2 = 0
f = 1
num = 0
for i in range(n):
    num += a[i]
    if f:
        if num >= 0:
            ans_2 += abs(-1 - num)
            num = -1
        f = 0
    else:
        if num <= 0:
            ans_2 += 1 - num
            num = 1
        f = 1

print(min(ans,ans_2))
        
            
