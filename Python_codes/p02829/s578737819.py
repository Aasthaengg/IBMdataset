a = int(input())
b = int(input())
ns = [1, 2, 3]
ns = [n for n in ns if not n == a and not n == b]
print(ns[0])