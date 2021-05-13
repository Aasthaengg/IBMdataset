s = input().rstrip().split(' ')
a = int(s[0])
b = int(s[1])
div = int(a / b)
module = a % b
divf = float(a / b)
print(str(div) + " " + str(module) + " " +"{0:.6f}".format(divf))