from bisect import bisect_right

x = int(input())
l = []

for i in range(2, 10):
    j = 1
    while j ** i <= 1000:
        y = j ** i
        if y not in l:
            l.append(y)
        j += 1

l.sort()
print(l[bisect_right(l, x)-1])