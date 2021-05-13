n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
    if (a[i] == b[i] and a[i] != c[i]) or\
        (a[i] == c[i] and a[i] != b[i]) or\
        (b[i] == c[i] and b[i] != a[i]):
        ans += 1
    elif a[i] == b[i] == c[i]:
        continue
    else:
        ans += 2
print(ans)