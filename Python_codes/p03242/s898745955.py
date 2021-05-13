n = input()
print(n.replace('1','X').replace('9','1').replace('X','9') if "1"or'9' in n else n)