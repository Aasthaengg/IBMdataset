s = input()
t = input()
n_s = len(s)
n_t = len(t)

ans_li = []
for i in range(n_s-n_t+1):
    u = s[i:i+n_t]
    flag = True
    for j in range(len(u)):
        if (u[j]!='?' and u[j]==t[j]) or u[j]=='?':
            continue
        flag = False
    if flag:
        ans_li.append(s[:i].replace('?','a')+t+s[i+n_t:].replace('?','a'))
if ans_li==[]:
    print('UNRESTORABLE');exit()
ans_li.sort()
print(ans_li[0])