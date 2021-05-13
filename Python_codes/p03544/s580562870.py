n = int(input())
l = []
if n == 0:
    l.append(2)
elif n == 1:
    l.append(1)
elif n >= 2:
    l = [2, 1]
    for i in range(2, n+1):
        l.append(l[i-2]+l[i-1])
print(l[-1])