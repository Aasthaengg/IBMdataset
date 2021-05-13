s = input()
anum, bnum, cnum = 0, 0, 0
for i in range(len(s)):
    si = s[i]
    if si == 'a':
        anum += 1
    elif si == 'b':
        bnum += 1
    else:
        cnum += 1
mini = min(anum, bnum, cnum)
anum, bnum, cnum = anum-mini, bnum-mini, cnum-mini

lst = [anum, bnum, cnum]
lst.sort()
dai = lst[2]
sho = lst[0]
mid = lst[1]

if dai==0 and mid==0:
    ans = 'YES'
elif dai>0 and mid==0:
    if dai == 1:
        ans = 'YES'
    else:
        ans = 'NO'
elif dai>0 and mid>0:
    if dai == 1:
        ans = 'YES'
    else:
        ans = 'NO'
print(ans)