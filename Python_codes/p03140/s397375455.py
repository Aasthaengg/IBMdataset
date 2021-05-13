n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
    tmp = 0
    if a[i] == b[i]:
        tmp += 1
    if a[i] == c[i]:
        tmp += 1
    if b[i] == c[i]:
        tmp += 1
    if tmp == 1:
        ans += 1
    elif tmp == 0:
        ans += 2
print(ans)