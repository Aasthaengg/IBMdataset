n, k = map(int, input().split())
a = list(map(int, input().split()))
x=bin(k)[2:]

ans=0
flag=True

for i in range(50):
    count=0
    for j in range(n):
        if (a[j]>>(50-i-1))&1==1:
            count+=1

    if 50-i-1>len(x)-1:
        ans+=2**(50-i-1)*count

    elif not flag:
        ans+=2**(50-i-1)*max(count, n-count)
    else:
        if 2*count>=n:
            if int(x[-(50 - i)]) == 1:
                ans+=2**(50-i-1)*count
                flag=False
            else:
                ans += 2 ** (50 - i - 1) * count
        
        else:
            if int(x[-(50-i)])==1:
                ans+=2**(50-i-1)*(n-count)
            else:
                ans+=2**(50-i-1)*count

print(ans)
