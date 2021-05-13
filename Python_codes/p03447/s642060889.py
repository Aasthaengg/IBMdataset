X = int(input())
A = int(input())
B = int(input())

Y = (X - A) // B
answer = X - A - (B * Y)
print(answer)