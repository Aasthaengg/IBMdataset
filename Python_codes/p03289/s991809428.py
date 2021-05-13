S = list(input())
l = [chr(i) for i in range(65, 65+26)]

flag = True
count = 0
for i in range(len(S)):
    if i == 0:
        if S[i] != 'A':
            flag = False
            break
    if i == 1:
        if S[i] in l:
            flag = False
            break
    if 2 <= i <= len(S) - 2:
        if S[i] == 'C':
            count += 1
        elif S[i] in l:
            flag = False
            break
    if i == len(S) - 1:
        if S[i] in l:
            flag = False
            break
if not count == 1:
    flag = False

if flag:
    print('AC')
else:
    print('WA')