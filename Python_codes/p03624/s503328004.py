s = str(input())
moji = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i in range(len(moji)):
    dic.setdefault(moji[i],0)
for i in range(len(s)):
    dic[s[i]] += 1
isNone = True
for i in range(len(moji)):
    if dic[moji[i]]==0:
        print(moji[i])
        isNone = False
        break
if isNone:
    print('None')