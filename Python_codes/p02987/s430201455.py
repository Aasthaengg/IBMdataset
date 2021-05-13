S = input()
dic = {}
flag = 0

for i in range(4):
    if S[i] in dic:
        dic[S[i]] += 1
    else:
        dic[S[i]] = 1

for v in dic.values():
    if v != 2:
        flag += 1

if flag == 0:
    print('Yes')
else:
    print('No')
