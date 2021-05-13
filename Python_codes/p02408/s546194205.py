n = int(input())
list =['1','2','3','4','5','6','7','8','9','10','11','12','13']
S_list = list.copy()
H_list = list.copy()
C_list = list.copy()
D_list = list.copy()
for i in range(n):
    a = input()
    b = a.split(' ')
    if b[0] == 'S':
        S_list.remove('%s'%(b[1]))
    elif b[0] == 'H':
        H_list.remove('%s'%(b[1]))
    elif b[0] == 'C':
        C_list.remove('%s'%(b[1]))
    elif b[0] == 'D':
        D_list.remove('%s'%(b[1]))
for i in S_list:
    print('S '+i)
for e in H_list:
    print('H '+e)
for f in C_list:
    print('C '+f)
for g in D_list:
    print('D '+g)