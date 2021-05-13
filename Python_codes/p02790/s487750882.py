a, b = input().split()
print(int(a * int(b)) if int(a * int(b)) > int(b * int(a)) else int(b * int(a)) )