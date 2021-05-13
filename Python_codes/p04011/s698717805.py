l=[int(input()) for i in range(4)]

if(l[0]>l[1]):
    a=l[1]*l[2]+(l[0]-l[1])*l[3]
else:
    a=l[0]*l[2]

print(a)