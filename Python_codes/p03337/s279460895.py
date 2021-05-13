num = input()
a = int(num.split(' ')[0])
b = int(num.split(' ')[1])


c = [a+b,a-b,a*b]

print(max(c))
