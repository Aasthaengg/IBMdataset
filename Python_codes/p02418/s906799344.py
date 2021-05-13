hoge = list()
for _ in range(2):
    hoge.append(input())
hoge[0] = hoge[0] + hoge[0]
if hoge[0].find(hoge[1]) == -1:
    print ('No')
else:
    print ('Yes')
