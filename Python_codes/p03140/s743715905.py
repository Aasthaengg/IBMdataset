n = int(input())
a = tuple(map(str, input()))
b = tuple(map(str, input()))
c = tuple(map(str, input()))
ans = 2*n
for i in range(n):
    if a[i] == b[i] == c[i]:
        ans -= 2
        continue
    elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
        ans -= 1
print(ans)