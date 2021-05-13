s = input()
t = input()
s1 = sorted(s)
t1 = sorted(t,reverse=True)

flag = -10
for i in range(min(len(s) , len(t))):
    if s1[i] < t1[i]:
        flag = 1
        break
    elif s1[i] == t1[i]:
        continue
    elif s1[i] > t1[i]:
        flag = 2
        break

if (flag == -10) and (len(s) < len(t)):
    print('Yes')
    
if (flag == -10) and (len(s) >= len(t)):
    print('No')
    
if flag == 1:
    print('Yes')
if flag == 2:
    print('No')