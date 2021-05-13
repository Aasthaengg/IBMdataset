n = int(input())

if n%10 == 0: print(10)
else: print(sum([int(i) for i in str(n)]))
