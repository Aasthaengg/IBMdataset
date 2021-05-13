string = input()
print(max(eval(string.replace(" ", op)) for op in ["+", "-", "*"]))