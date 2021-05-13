a, b = map(int, input().split())
c = a + b

if a % 3 and b % 3 and c % 3:
    print("Impossible")
else:
    print("Possible")
