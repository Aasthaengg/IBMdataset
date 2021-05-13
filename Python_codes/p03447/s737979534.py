count = int(0)

X = int(input())
A = int(input())
B = int(input())

zankin = int(X - A)


while zankin >= B:
    zankin = zankin - B
    count = count + 1
  

b = B * count

zankin2 = X - A - b

print(zankin2)
