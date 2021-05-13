n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
prev = -10
for i in range(n):
    ind = a[i] - 1
    ans += b[ind]
    if prev + 1 == ind:
        ans += c[prev]
    prev = ind
print(ans)