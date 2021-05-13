s = input()

a = 0
l = []

for i in s:
    if a == 0:
        if i == "<":
            a = 1
        else:
            a = -1
    elif ((a > 0) and i == "<"):
        a += 1
    elif ((a < 0) and i == ">"):
        a -= 1
    elif i == "<":
        l.append(a)
        a = 1
    else:
        l.append(a)
        a = -1
l.append(a)

m=[]

for j in l:
    if m:
        if j > 0:
            m.pop()
            for k in range(0, abs(j) + 1, 1):
                m.append(k)
        else:
            b = m.pop()
            if b > abs(j) - 1:
                m.append(b)
                for k in range(abs(j) -1, -1, -1):
                    m.append(k)
            else:
                for k in range(abs(j), -1, -1):
                    m.append(k)
    else:
        if j > 0:
            for k in range(0, abs(j) + 1, 1):
                m.append(k)
        else:
            for k in range(abs(j), -1, -1):
                m.append(k)
            
print(sum(m))