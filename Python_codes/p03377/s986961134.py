line = input()
a, b, x = [int(n) for n in line.split()]

largest = 0

z = a+b+x

if x < a:
    print("NO")
elif x > a+b:
    print("NO")
elif x <= a+b:
    print("YES")

