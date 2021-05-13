n = int(input())
a_dic = {}
for i in range(n):
    a = int(input())
    if a in a_dic:
        a_dic.pop(a)
    else:
        a_dic[a] = 1
        

print(len(a_dic))