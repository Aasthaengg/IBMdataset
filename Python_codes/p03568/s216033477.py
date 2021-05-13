n = int(input())
a = list(map(int, input().split()))
even_cnt = []
for i in range(n):
    if a[i]%2==0:
        even_cnt.append(1)
        a[i] = 2
    else:
        even_cnt.append(2)
        a[i] = 1
x = 3 ** n
ans = 0
for i in range(n):
    x //= 3
    ans += even_cnt[i]*x
    x *= a[i]
print(ans)