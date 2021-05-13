MOD=1000000007

N = int(input())
a = list(input())
b = list(input())

ans = 1
pre = 0
i=0
if a[i]!=b[i]:
    ans = 6
    i+=2
    pre = 2
else:
    ans = 3
    i+=1
    pre = 1

while i < N:
    if a[i]!=b[i]:
        if pre==1:
            ans = ans*2
            ans = ans%MOD
            i+=2
            pre = 2
        else:
            ans = ans*3
            ans = ans%MOD
            i+=2
            pre = 2
    else:
        ans = ans*(3-pre)
        ans = ans%MOD
        i+=1
        pre = 1

print(ans)