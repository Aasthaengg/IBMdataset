s = input()
dic = {}
flag = True
for i in range(len(s)):
    if s[i] not in dic.keys():
        dic[s[i]] = 1
    else:
        flag = False
if flag:
    print("yes")
else:
    print("no")