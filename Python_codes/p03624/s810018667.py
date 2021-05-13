str1 = input()
li = list(str1)
anli = []
for i in range(26):
    anli.append(0)
for i in range(len(li)):
   anli[ord(li[i]) - 97] += 1
flag = True
mi = 27
for i in range(len(anli)):
    if anli[i] == 0:
        flag = False
        mi = min(i,mi)
if flag:
    print('None')
else:
    print(chr(mi+97))