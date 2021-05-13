input_line = input()
a,b,c = input_line.strip().split(' ')
a = int(a)
b = int(b)
c = int(c)

if a < b < c:
    print("Yes")
else:
    print("No")