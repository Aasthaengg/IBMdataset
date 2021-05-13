s = list(input())
l = ['K','I','H','B','R',-1]
j = 0
 
for i in range(len(s)):
    if s[i] == 'A':
        if i == 0:
            pass
        elif s[i-1] == 'A':
            print('NO')
            exit(0)
        elif j == 1 or j == 2:
            print('NO')
            exit(0)
        else:
            pass
    elif s[i] != l[j]:
        print('NO')
        exit(0)
    else:
        j += 1
 
if j == 5:
    print('YES')
else:
    print('NO')