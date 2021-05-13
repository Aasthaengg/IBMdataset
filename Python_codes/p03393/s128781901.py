s = input()
alf = 'abcdefghijklmnopqrstuvwxyz'
pos = {}
pos_alf = {c:i for i,c in enumerate(alf)}

for i,c in enumerate(s):
    if c not in pos:
        pos[c] = []
    pos[c] = i

# if s == 'zyxwvutsrqponmlkjihgfedcba':
#     print(-1)
#     exit()
# el
if len(s) != 26:
    for c in alf:
        if c not in pos:
            print(s+c)
            exit()

tmp = [pos_alf[s[-1]]]
for i in range(len(s)-1)[::-1]:
    if pos_alf[s[i]] < max(tmp):
        d = [j for j in tmp if j > pos_alf[s[i]]]
        print(s[:i]+alf[min(d)])
        break
    else:
        tmp.append(pos_alf[s[i]])
    # print(tmp)
else:
    print(-1)
