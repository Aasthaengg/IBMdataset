a, b = map(int, input().split())

A = str(a) * b
B = str(b) * a

AB = [A,B]

print(min(AB))