dic = {}
dic.setdefault('a',str(input())+'E')
dic.setdefault('b',str(input())+'E')
dic.setdefault('c',str(input())+'E')
dare = dic['a'][0]
dic['a'] = dic['a'][1:]
while len(dic['a'])>0 and len(dic['b'])>0 and len(dic['c'])>0:
    tmp = dic[dare][0]
    dic[dare] = dic[dare][1:]
    if tmp=='E':
        ans = dare.upper()
    dare = tmp
print(ans)
