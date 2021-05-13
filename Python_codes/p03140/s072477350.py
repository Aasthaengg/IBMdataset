n = int(input())
a = list(input())
b = list(input())
c = list(input())

cnt = 0

for i in range(n):
    if a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
        cnt += 2
    elif a[i] == b[i] and a[i] == c[i] and b[i] == c[i]:
        cnt += 0
    else:
        cnt += 1

print(cnt)
