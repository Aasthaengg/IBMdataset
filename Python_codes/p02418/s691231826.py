s=raw_input()
p=raw_input()

hits=[]
for j in range(len(s)):
    if p[0] == s[j]:
        hits.append(j)


flg=False
_i = 0
for _j in hits:
    if flg: break
    j=_j
    while True:
        for idx, i in enumerate(range(_i, len(p))):
            if j + i > len(s) -1:
                break 
            if p[i] == s[j+idx]:
                flg=True
            else:
                flg=False
                break
        else:
            break

        if flg:
            j = 0
            _i = i
        else:
            break

if flg:
    print "Yes"
else:
    print "No"