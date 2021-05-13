N=input()
lst=[]
for i in N:
    if i=='1':
        lst.append('9')
    else:
        lst.append('1')
print(''.join(lst))