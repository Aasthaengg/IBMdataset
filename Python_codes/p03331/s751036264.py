n = input()

powers10 = [10**i for i in range(1, 6)]
print(10 if int(n) in powers10 else sum(int(d) for d in n))
