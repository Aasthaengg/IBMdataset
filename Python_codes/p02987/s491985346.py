s=input()
s1=[]
for i in s:
    if i not in s1:
        s1.append(i)
if len(s1)==2:
    print('Yes')
else:

    print('No')