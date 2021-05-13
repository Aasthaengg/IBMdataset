s = str(input())
dic = {}
dic.setdefault('a',0)
dic.setdefault('b',0)
dic.setdefault('c',0)
    
for i in range(len(s)):
    dic.setdefault(s[i],0)
    dic[s[i]] += 1

if dic['a']==1 and dic['b']==1 and dic['c']==1:
    print('Yes')
else:
    print('No')
