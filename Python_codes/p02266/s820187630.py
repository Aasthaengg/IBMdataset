dan = list(input())
wid = len(dan)
stack_s1 = list()
stack_s2 = list()

for i in range(wid):
    if dan[i] == '\\':
        stack_s1.append(i)
    if len(stack_s1) > 0 and dan[i] == '/':
        j = stack_s1.pop()
        men = i - j
        while len(stack_s2) > 0 and j < stack_s2[-1][0]:
            tmp = stack_s2.pop()
            men += tmp[1]
        stack_s2.append([j, men])

t_men = 0
k = list()
k.append(str(len(stack_s2)))
for i, j in stack_s2:
    t_men += j
    k.append(str(j))
print(t_men)
print(' '.join(k))

