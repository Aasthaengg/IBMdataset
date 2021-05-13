s = str(input())
n = len(s)

X = ['']
temp = ''
for i in range(n):
    temp += s[i]
    if temp == X[-1]:
        continue
    else:
        X.append(temp)
        temp = ''
else:
    if temp != '':
        if temp == X[-1]:
            X[-1] += temp
        else:
            X.append(temp)

#print(X)
print(len(X)-1)
