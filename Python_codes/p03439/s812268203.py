N = int(input())
ss = 0
se = N-1
print(ss,'\n')
sf = input()
if sf == 'Vacant':
    exit(0)
while True:
    if se - ss == 1:
        q = se
    else:   
        q=(ss+se)//2
    print(q,'\n')
    s = input()
    if s == 'Vacant':
        exit(0)
    elif (s == sf and (q-ss+1)%2==1 ) or (not s == sf and (q-ss+1)%2==0):
        ss = q
        sf = s
    else:
        se = q
