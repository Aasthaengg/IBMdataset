table = {alphabet: "-" for alphabet in "abcedfghijklmnopqrstuvwxyz"}
rev_table = {alphabet: "-" for alphabet in "abcedfghijklmnopqrstuvwxyz"}

s = str(input())
t = str(input())

flag = True

for i in range(len(s)):
    if table[s[i]] == t[i]:
        continue
    elif table[s[i]] == "-":
        table[s[i]] = t[i]
    else:
        flag = False
        break

for i in range(len(t)):
    if rev_table[t[i]] == s[i]:
        continue
    elif rev_table[t[i]] == "-":
        rev_table[t[i]] = s[i]
    else:
        flag = False
        break

if flag is True:
    print("Yes")
else:
    print("No")
