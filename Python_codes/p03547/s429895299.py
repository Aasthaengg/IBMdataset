x,y = map(str,input().split())
dic = {}
dic.setdefault('A',1)
dic.setdefault('B',2)
dic.setdefault('C',3)
dic.setdefault('D',4)
dic.setdefault('E',5)
dic.setdefault('F',6)
if dic[x]<dic[y]:
    print('<')
elif dic[x]>dic[y]:
    print('>')
else:
    print('=')