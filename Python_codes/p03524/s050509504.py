s = list(input())
t = set(s)
if(len(t) == 1):
    if(len(s) == 1):
        print('YES')
    else:
        print('NO')
elif(len(t) == 2):
    if(len(s) == 2):
        print('YES')
    else:
        print('NO')
else:
    n = [0,0,0]
    for i in s:
        if(i == 'a'):n[0] +=1
        if(i == 'b'):n[1] +=1
        if(i == 'c'):n[2] +=1
    n.sort()
    n[1] -= n[0]
    n[2] -= n[0]
    n[0] -= n[0]
    if(n[1] <= 1 and n[2] <= 1):
        print('YES')
    else:
        print('NO')


