a, b = map(int, input().split())
A = sum([i for i in range(b-a)])
B = sum([i for i in range(b-a+1)])
print(A-a)
