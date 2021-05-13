n, T  = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
till = 0

for i in t:
    if i < till:
        temp = T - (till - i)
        ans += temp
        till += temp
    else:
        ans += T
        till = i + T

print(ans)