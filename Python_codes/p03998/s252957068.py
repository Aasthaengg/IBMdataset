dic = {}
dic.setdefault('a',str(input())+'A')
dic.setdefault('b',str(input())+'B')
dic.setdefault('c',str(input())+'C')
dare = dic['a'][0]
dic['a'] = dic['a'][1:]
while len(dic['a'])>0 and len(dic['b'])>0 and len(dic['c'])>0:
    tmp = dic[dare][0]
    dic[dare] = dic[dare][1:]
    dare = tmp
print(dare)
