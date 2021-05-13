s = input()
p = input()
tmp_s = s
flag = False
for i in range(len(s)):
    tmp_s = tmp_s[-1]+tmp_s[0:-1]
    if tmp_s.count(p)>0:
        flag = True
        break
    else:
        pass
if flag:
    print("Yes")
else:
    print("No")