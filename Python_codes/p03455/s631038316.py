a = input()
b = a.split(' ')
 
nummm = 1
 
for l in b:
    nummm = int(nummm) * int(l)
 
if int(nummm) % 2 == 0:
    print('Even')
else:
    print('Odd')