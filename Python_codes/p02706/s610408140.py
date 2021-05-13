mn = input().split()

n = int(mn[0])
m = mn[1]

ms = input().split()

for i in range(int(m)):
    n -= int(ms[i])

if n < 0:
    print("-1")

else:
    print(n)