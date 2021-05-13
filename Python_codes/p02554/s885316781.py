n = int(input())
a = 10 ** n - 9 ** n
b = 10 ** n - 8 ** n 
print((2*a - b) % (10**9 + 7))
