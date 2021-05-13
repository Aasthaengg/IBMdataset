line = input()

a, b = [int(n) for n in line.split()]

apb = a+b
asb = a-b
atb = a*b

print(max(apb, asb, atb))