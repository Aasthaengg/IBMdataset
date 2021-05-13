x = int(input())
a = int(input())
b = int(input())

xa = x - a
xab = xa // b
answer = xa - (b * xab)

print(answer)