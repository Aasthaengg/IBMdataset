line = input()
a, b, x = [int(n) for n in line.split()]

if x>(a+b) or x<a:
    print("NO")
else:
    print("YES")