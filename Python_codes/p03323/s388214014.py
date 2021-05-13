num = input()
a = int(num.split(' ')[0])
b = int(num.split(' ')[1])

if a > 8 or b > 8:
    print(":(")
else:
    print("Yay!")
