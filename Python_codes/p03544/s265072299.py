n = int(input())
l = [2, 1]
for i in range(n-1):
    l.append(0)

if n >= 2:
    for i in range(2, n+1):
        l[i] = l[i-1] + l[i-2]
print(l[n])
