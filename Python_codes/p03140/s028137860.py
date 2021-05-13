n = int(input())
a = list(input())
b = list(input())
c = list(input())
ans = 0
for i in range(n):
    l = [a[i],b[i],c[i]]
    l = list(set(l))
    if len(l) == 3:
        ans += 2
    elif len(l) == 2:
        ans += 1
    else:
        pass
print(ans)