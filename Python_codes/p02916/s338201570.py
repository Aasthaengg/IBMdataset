n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
res = 0
for i in range(n):
    num = a[i]
    res += b[num - 1]
for i in range(n-1):
    if a[i] +1== a[i+1] :
        num = a[i]
        res += c[num-1]
print(res)
