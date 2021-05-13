N = int(input())
s = input()

dic = dict()
for chr in s:
    if chr not in dic: 
        dic[chr] = 1
    else:
        dic[chr] += 1

if dic['R'] > dic['B']:
    print('Yes')
else:
    print('No')