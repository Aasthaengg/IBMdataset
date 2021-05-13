import fractions

n = int(input())
a = sorted(list(map(int, input().split())), reverse = True)

last = a[0]

for i in range(1, n):
    last = fractions.gcd(last, a[i])

print(last)