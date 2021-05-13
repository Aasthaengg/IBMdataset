n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
    x = len({a[i], b[i], c[i]})
    ans += x - 1
print(ans)