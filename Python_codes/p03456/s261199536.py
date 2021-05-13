a, b = map(str, input().split())

number = [i**2 for i in range(2,317,1)]
num = int(a + b)

if num in number:
    print("Yes")
else:
    print("No")


