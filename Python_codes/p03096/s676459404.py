n = int(input())
l = [0 for i in range(2*(10**5)+1)]
a = [1]
co = 0
for i in range(n):
    k = int(input())
    b = a[-1]
    if l[k] != i and l[k] != 0:
        b += a[l[k]]
    l[k] = i+1
    a.append(b%(10**9+7))
print(a[-1])