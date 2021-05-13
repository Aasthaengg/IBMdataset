n,m = map(int,input().split())
s,c = [0]*m,[0]*m
for i in range(m):
    s[i],c[i] = map(int,input().split())
    s[i] -= 1
number = ['0']*n
for j in range(m):
    if number[s[j]] != '0' and number[s[j]] != str(c[j]):
        print('-1')
        quit()
    elif s[j] == 0 and c[j] == 0 and n != 1:
        print('-1')
        quit()
    else:
        number[s[j]] = str(c[j])
else:
    if number[0]  == '0' and  n != 1:
        number[0] = '1'

print(''.join(number))