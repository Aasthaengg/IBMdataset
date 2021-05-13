s = input()
ans = 0
L = []
flag = False
for i in range(len(s)):
    if not flag:
        if i != len(s)-1 and s[i] == 'B':
            flag = True
        else:
            L.append(s[i])
    else:
        if s[i] == 'C':
            L.append('D')
        else:
            L.append('B')
            L.append(s[i])
        flag = False
new = []
num = []
flag = False
L.append('B')
for i in range(len(L)):
    if L[i] == 'A' and flag == False:
        setnum = 1
        flag = True
        cur = ['A']
    else:
        if flag == False:
            None
        else:
            if L[i] == 'B' or L[i] == 'C':
                flag = False
                new.append(cur)
                num.append(setnum)
            else:
                if L[i] == 'A':
                    cur.append('A')
                    setnum += 1
                else:
                    cur.append('D')
for i in range(len(new)):
    T = new[i]
    add = num[i]
    cur = 0
    for j in range(len(T)):
        if T[len(T)-j-1] == 'D':
            cur += add
        else:
            add -= 1
    ans += cur
print(ans)
