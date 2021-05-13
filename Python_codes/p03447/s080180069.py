X = int(input())
A = int(input())
B = int(input())

q, r = divmod(X - A, B)
print(r)