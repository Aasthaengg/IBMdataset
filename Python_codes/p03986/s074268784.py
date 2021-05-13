x = input()
s_q = []
arc = []
for i, v in enumerate(x):
    if v == 'S':
        s_q.append(v)
    else:
        if len(s_q) > 0:
            s_q.pop()
        else:
            arc.append(v)
print(len(s_q)+len(arc))

