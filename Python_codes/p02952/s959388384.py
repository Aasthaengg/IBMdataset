N = int(input())

if 1 <= N < 10:
    print(N)
elif 10 <= N < 100:
    print(9)
elif 100 <= N < 1000:
    print((N-100+1)+9)
elif 1000 <= N < 10000:
    print(9+900)
elif 10000 <= N < 100000:
    print((N-10000+1)+900+9)
else:
    print(90000+900+9)
