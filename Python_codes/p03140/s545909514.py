n = int(input())
a = input()
b = input()
c = input()

ans = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        continue
    elif a[i] != b[i] and b[i] != c[i] and c[i] != a[i]:
        ans += 2
    else:
        ans += 1
print(ans)
