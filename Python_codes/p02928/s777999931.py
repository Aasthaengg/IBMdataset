n,k = map(int, input().split())
a =  list(map(int, input().split()))
b,c = [0 for i in range(n)],[0 for i in range(n)]
num,wa = 10**9 +7,k * (k-1) //2
for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            b[i] += 1
            c[i] += 1
        elif a[i] < a[j]:
            c[j] += 1
ans = sum(c) * wa % num
ans += sum(b) * k
print(ans % num)
