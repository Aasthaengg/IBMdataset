n = input().split()
a = int(n[0])
b = int(n[2])
r = a + b if n[1] == '+' else a - b
print(r)