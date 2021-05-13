a=int(input())
b=input()
c=list(b.split(' '))
c.sort()
for i in range(0,len(c)-1):
    if c[i]==c[i+1]:
        print('NO')
        break
    if i==len(c)-2:
        print('YES')