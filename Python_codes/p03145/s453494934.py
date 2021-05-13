a, b, c = input().split()
x = [a, b, c]
x = [int(i) for i in x]
x.sort()
print(int((int(x[0])*int(x[1]))/2))