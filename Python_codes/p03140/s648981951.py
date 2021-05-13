n = int(input())

a = input()
b = input()
c = input()

t = 0
for i in range(n):
    s = set()
    s.add(a[i])
    s.add(b[i])
    s.add(c[i])
    t += len(s) - 1
print(t)