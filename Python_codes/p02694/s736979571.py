X = int(input())
o = 100
y = 0
 
while X > o:
    if o >= X:
        break
    else:
        o += o // 100
        y += 1
print(y)