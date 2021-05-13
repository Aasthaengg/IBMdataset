n = int(input())
d = 100000
for i in range(n):
    d *= 1.05
    d = d - (d - 1) % 1000 + 999
print(int(d))