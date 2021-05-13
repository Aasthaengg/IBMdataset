n = input()
a = sum([int(n[i]) for i in range(len(n))])
if a==1:
    print(10)
else:
    print(a)