n = int(input())
a = input()
b = input()
c = input()
res = 0
for i in range(n):
    if a[i] == b[i] == c[i]:
        pass
    elif a[i] == b[i]  and b[i] != c[i]:
        res += 1
    elif a[i] != b[i] and b[i] == c[i]:
        res += 1
    elif a[i] == c[i] and b[i] != c[i]:
        res += 1
    else:
        res += 2
print(res)