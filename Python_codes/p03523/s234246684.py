s = input()
n = 4

#AKIHABARAのAの箇所は4か所。それをbit全探索で一致するパターンがあるか判定
for i in range(2**n):
    tmp = ['','','','']
    for j in range(n):
        if ((i>>j)&1):
            tmp[j]='A'
    t = '{0[0]}KIH{0[1]}B{0[2]}R{0[3]}'.format(tmp) 
    if t==s:
        print('YES');exit()
print('NO')