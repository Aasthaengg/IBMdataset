from collections import defaultdict
s = input()
t = input()
n = len(s)
changed_s = defaultdict(list)
changed_t = defaultdict(list)
flag = True
used = []
for i in range(n):
    if s[i] != t[i]:
        changed_s[s[i]].append(t[i])
        changed_t[t[i]].append(s[i])
    else:
        used.append(s[i])

#print(changed_s)
#print(changed_t)
#print(used)
for key, lis in changed_s.items():
    if len(set(lis)) == 1 and key in used:
        flag = False
    elif len(set(lis)) != 1:
        flag = False
for key, lis in changed_t.items():
    if len(set(lis)) == 1 and key in used:
        flag = False
    elif len(set(lis)) != 1:
        flag = False
if flag:
    print("Yes")
else:
    print("No")