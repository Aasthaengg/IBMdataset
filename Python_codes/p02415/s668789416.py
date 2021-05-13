x = input()

y = ""
for i in range(0,len(x)):
    if x[i] >= 'a' and x[i] <= 'z':
        y += x[i].upper()
    else:
        y += x[i].lower()
print(y)
