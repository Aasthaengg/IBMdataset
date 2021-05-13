a = [int(input()) for _ in range(3)]
num = a[2]/max(a[0], a[1])
if num.is_integer():
    print(int(num))
else:
    print(int(num)+1)
