s = input()
#Aの海をかき分けてBCが進む

r = list(reversed(list(s)))
r = ['X'] + r + ['X']
#print(r)
BC_cnt = 0
A_cnt = 0
cnt = 0
for i in range(1, len(s) + 1):
    if r[i] == 'A':
        cnt += BC_cnt
        #print(BC_cnt, A_cnt)
    elif r[i] == 'C' and r[i + 1] == 'B':
        BC_cnt += 1
    elif r[i - 1] == 'C' and r[i] == 'B':
        pass
    else:
        BC_cnt = 0
print(cnt)
