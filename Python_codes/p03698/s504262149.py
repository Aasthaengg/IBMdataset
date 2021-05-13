str1 = input()
li = list(str1)
flag = False
for i in range(len(li)):
    a = i+1
    x = li[i]
    while a < len(li):
        if x == li[a]:
            flag = True
            break
        a += 1
    if flag:
        break
if flag:
    print('no')
else:
    print('yes')