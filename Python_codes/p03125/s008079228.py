num = input().split()
a, b = int(num[0]), int(num[1])
if b%a==0: print(a+b)
else: print(b-a)