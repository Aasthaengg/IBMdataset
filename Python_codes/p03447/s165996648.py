X = int(input())
A = int(input())
B = int(input())

c = (X - A) // B
ans = X - A - B * c
print(ans)