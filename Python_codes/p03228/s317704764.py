def spliter(a):
    a = str(a)
    b = list()
    b = a.split(' ')
    for i in range(0,len(b)):
        b[i] = int(b[i])
    return b
s = spliter(str(input()))
goal = s[2]
counter = 0
while counter != goal:
    if s[0] % 2 == 0:
        s[1] += (s[0] / 2)
        s[0] -= (s[0] / 2)
        counter += 1
        if counter == goal:
            break
        else:
            if s[1] % 2 == 0:
                s[0] += (s[1] / 2)
                s[1] -= (s[1] / 2)
                counter += 1
                if counter == goal:
                    break
            else:
                s[1] -= 1
                s[0] += (s[1] / 2)
                s[1] -= (s[1] / 2)
                counter += 1
                if counter == goal:
                    break
    else:
        s[0] -= 1
        s[1] += (s[0] / 2)
        s[0] -= (s[0] / 2)
        counter += 1
        if counter == goal:
            break
        else:
            if s[1] % 2 == 0:
                s[0] += (s[1] / 2)
                s[1] -= (s[1] / 2)
                counter += 1
                if counter == goal:
                    break
            else:
                s[1] -= 1
                s[0] += (s[1] / 2)
                s[1] -= (s[1] / 2)
                counter += 1
                if counter == goal:
                    break
            
print(int(s[0]),int(s[1]))
