sd = input()
t = input()

anss = []
for tpos in range(len(sd) - len(t) + 1):
    check = True
    for i in range(len(t)):
        if t[i] != sd[(i + tpos)] and sd[(i + tpos)] != '?':
            check = False
            break
    if check == True:
        cand = sd[:tpos] + t + sd[(tpos + len(t)):]
        anss.append(cand.replace('?', 'a'))

if len(anss) == 0:
    print('UNRESTORABLE')
else:
    print(sorted(anss)[0])
