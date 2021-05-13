t = int(input())
a = 100000
for i in range(t):
        a = a * 1.05
        if a % 1000:
                a = a - (a % 1000) + 1000
print(int(a))
