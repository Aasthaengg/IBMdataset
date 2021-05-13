A = input().split()
S = []


for i in A:
    if i == '+' or i == '-' or i == '*':
        a = S.pop()
        b = S.pop()
        if i == '+': S.append(b+a)
        elif i == '-': S.append(b-a)
        else: S.append(b*a)
    else:
        x = int(i)
        S.append(x)
    #print(S)

print(S[0])
