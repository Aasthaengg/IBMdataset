n = int(input())

a = []

for i in range(1, n+1):
    if(i * i > n):
        break
    if(n % i == 0):
        a.append(int(n / i) + i)


a.sort()

print(a[0] - 2)
