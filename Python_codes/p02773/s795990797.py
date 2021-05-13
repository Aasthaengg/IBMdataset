n = int(input())
dic = {}

for i in range(n):
    s = input()
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

C = sorted(dic.items())
max_dic = max(dic.values())

for name,i in C:
    if i == max_dic:
        print(name)