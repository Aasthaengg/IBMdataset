n = int(input())
a = 1
ans = 0
if a >= n:
    ans = 1
else:
    for i in range(2,n+1):
        a += i
        if a >= n:
            ans = i
            break
for k in range(1,ans+1):
    if a - n != k:
        print(k)
    else:
        continue