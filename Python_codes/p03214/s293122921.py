n = int(input())
a = list(map(int, input().split()))
b = sum(a)/n

ans = 0
for i in range(1,n):
    if abs(a[i]-b)<abs(a[ans]-b):
        ans = i
print(ans)