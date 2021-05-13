line = input()
a, b = [int(n) for n in line.split()]
if(a + b > 16):
    print(":(")
elif(a <= 8 and b <= 8):
    print("Yay!")
else:
    print(":(")