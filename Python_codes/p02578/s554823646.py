n = int(input())
a = list(map(int, input().split()))
b = a[0]
ans = 0
for i in a:
    if b < i:
        b = i
    else:
        ans += b-i
print(ans)