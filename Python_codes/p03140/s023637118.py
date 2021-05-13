n = int(input())
a = input()
b = input()
c = input()
count = 0
for i in range(n):
    ab = a[i] + b[i]
    bc = b[i] + c[i]
    ca = c[i] + a[i]
    count += 2 - max(ab.count(c[i]), bc.count(a[i]), ca.count(b[i]))
print(count)