a=int(input())
result=[]
for i in range(26):
    for j in range(26):
        result.append(i*4+j*7)

if a in result:
    print('Yes')
else:
    print('No')