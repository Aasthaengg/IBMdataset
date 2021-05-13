b = input()
number1 = ['A','T']
number2 = ['C','G']
print(number1[number1.index(b)-1]) if b in number1 else print(number2[number2.index(b)-1])