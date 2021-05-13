n,k = map(int, input().split())
a =  list(map(int, input().split()))
b,c = 0,0
num,wa = 10**9 +7,k * (k-1) //2
for i in range(n-1):
    for j in range(i+1,n):
        if a[i] != a[j]:
            c += 1
            if a[i] > a[j]:
                b += 1
ans = c * wa % num
ans += b * k
print(ans % num)
