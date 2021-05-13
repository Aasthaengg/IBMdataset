a, o, b = map(str, input().split())

if o == "+":
    operation = int(a) + int(b)
else:
    operation = int(a) - int(b)
print(operation)