n, a, b = map(int, input().split())
if n == 0 or b < a or (n == 1 and a != b):
    print(0)
elif n == 1 and a == b:
    print(1)
else:
    print(1+(b-a)*(n-2))