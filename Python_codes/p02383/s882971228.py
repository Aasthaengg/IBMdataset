d = list(map(int, input().split(' ')))
s = input()
L = [0,1,2]
for i in s:
    if i == 'E':
        a = 5 - L[2]
        b = L[1]
        c = L[0]
        L = [a, b, c]
    elif i == 'W':
        a = L[2]
        b = L[1]
        c = 5 - L[0]
        L = [a, b, c]
    elif i == 'N':
        a = L[1]
        b = 5 - L[0]
        c = L[2]
        L = [a, b, c]
    elif i == 'S':
        a = 5 - L[1]
        b = L[0]
        c = L[2]
        L = [a, b, c]
print(d[L[0]])
