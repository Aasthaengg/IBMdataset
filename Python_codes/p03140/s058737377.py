n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
    if a[i] == b[i] and b[i] == c[i]:
        ans += 2
    elif a[i] == b[i]:
        ans += 1
    elif b[i] == c[i]:
        ans += 1
    elif a[i] == c[i]:
        ans += 1
print(n*2-ans)