N = int(input())

a = N
S_list = []
if a == 0:
    S_list.append(a)
while a != 0:
    Si = a % (-2)
    a //= (-2)
    if Si == -1:
        a += 1
        Si = 1
    S_list.append(Si)


S = ''.join([str(i) for i in S_list[::-1]])
print(S)
