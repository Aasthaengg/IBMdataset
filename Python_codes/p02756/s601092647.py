s = input()
Q = int(input())

rev_count = 0
sbf=''
saf=''
for i in range(Q):
    que = input()
    if que[0] == '1':
        rev_count +=1
    elif que[0] == '2':
        if (rev_count + int(que[2]))%2 == 0:
            saf = saf + que[4]
        else:
            sbf = que[4] + sbf

print(sbf+s+saf if rev_count %2 == 0 else (sbf+s+saf)[-1::-1])
