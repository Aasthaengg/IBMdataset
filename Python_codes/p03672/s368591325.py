def evenstr(x):
    box1 = []
    box2 = []
    if len(x) % 2 == 1:
        return False
    else:
        v = int(len(x) / 2)
        for i in range(v):
            box1.append(x[i])
        for i in range(v, len(x)):
            box2.append(x[i])
        if box1 == box2:
            return True
        else:
            return False

    

count = 0
s = input()
p = list(s)
p.pop()
count += 1

for i in range(len(p) - 2):
    if evenstr(p):
        break
    else:
        count += 1
    p.pop()

print(len(p))
    


