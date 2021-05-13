ab=[]
ba=[]
fullpath=[]
for i in range(3):
    ab.append(list(map(int,input().split())))
for i in range(3):
    ba.append(list(reversed(ab[i])))
fullpath=ab+ba
fullpath1=[]
for i in range(len(fullpath)):
    fullpath1.append(fullpath[i][0])
count=[]
for i in range(1,5):
    count.append(fullpath1.count(i))
if count.count(1)==2 and count.count(2)==2:
    print('YES')
else:
    print('NO')