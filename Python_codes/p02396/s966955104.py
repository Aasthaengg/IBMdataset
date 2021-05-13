j=[]
while True:
    i=input()
    if i =='0':break
    j.append(i)

for i in range(1, len(j)+1):
    print('Case {0}: {1}'.format(i, j[i-1]))
