import  itertools

li = input().split()
if li[0]==li[1]==li[2]:
    print('No')
    exit()

p=itertools.permutations(li,2)

for i in p:
   if i[0] == i[1]:
        print('Yes')
        exit()
print('No')


