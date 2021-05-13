n = int(input())
a = list(map(int,input().split()))

ave = sum(a)/n
number = []
small = 10**3

for i in range(n):
    if abs(a[i] - ave) < small:
        number = []
        number.append(i)
        small = abs(a[i] - ave)

number.sort()

print(number[0])