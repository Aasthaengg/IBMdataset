a, b = map(int, input().split())

ab = a * b

ab_mod = ab % 2

if (ab_mod == 0 ):
    print("Even")

else:
    print("Odd")