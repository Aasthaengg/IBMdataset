n = int(input())
l = [2, 1]
for i in range(2, n+1):
    a = l[i-2] + l[i-1]
    l.append(a)
print(l[n])