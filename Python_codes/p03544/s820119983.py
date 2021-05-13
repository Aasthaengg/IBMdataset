n = int(input())
l = [2, 1]
if n == 1:
    print(1)
else:
    for i in range(n):
        l.append(l[i+1]+l[i])
    print(l[n])