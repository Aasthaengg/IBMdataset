s=[int(x) for x in input().split()]
ab=[input().split() for y in range(s[0])]
c=0
for z in ab:
    if(int(z[0])>=s[1] and int(z[1])>=s[2]):
       c+=1
print(c)