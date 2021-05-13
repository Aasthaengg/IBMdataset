n=int(input())
if n<10:
    print(n)
elif n<100:
    print("9")
elif n<1000:
    print(9+n-99)
elif n<10000:
    print("909")
elif n<100000:
    print(909+n-9999)
elif n==100000:
    print("90909")
