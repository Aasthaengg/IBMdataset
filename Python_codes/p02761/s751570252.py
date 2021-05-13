n,m = map(int,input().split())
s,c = [0]*m,[0]*m
for i in range(m):
    s[i],c[i] = map(int,input().split())
    s[i] -= 1
ans = ''
number = ['0']*n
for j in range(m):
    flag_1 = (number[s[j]] != '0' and number[s[j]] != str(c[j]))
    flag_2 = (s[j] == 0 and c[j] == 0 and n != 1)
    if flag_1 or flag_2:
        ans = '-1'
        break
    else:
        number[s[j]] = str(c[j])
else:
    if number[0]  == '0' and  n != 1:
        number[0] = '1'
    ans = ''.join(number)

print(ans)