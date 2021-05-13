n, k = map(int, input().split())
a = {}
p = 0
for i in range(n, 0, -1):
    b = 0
    j = i
    while j < k:
        if j in a:
            b += a[j]
            break;
        else:
            j *= 2
            b += 1
    a[i] = b
c = [0]*20
for i in range(n):
    c[a[i+1]] += 1
for i in range(20):
    p += c[i]*(1/2)**i
print(p/n)