s=input()
l='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    if(s.count(l[i])==0):
        print(l[i])
        exit()
print('None')