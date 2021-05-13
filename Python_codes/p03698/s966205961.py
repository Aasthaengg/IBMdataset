s = str(input())
w = []
x = 'yes'
for i in s:
    if i in w:
        x = 'no'
        break
    else:
        w.append(i)
print(x)