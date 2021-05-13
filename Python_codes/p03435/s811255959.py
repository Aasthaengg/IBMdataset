c=[0]*3
c_max=0
for i in range(3):
    c[i]=list(map(int,input().split()))
    c_max=max(c_max,max(c[i]))
c_max+=1
for a1 in range(c_max):
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1
    a2 = c[1][0] - b1
    a3 = c[2][0] - b1
    if a1+b1==c[0][0] and a1+b2==c[0][1] and a1+b3==c[0][2] and a2+b1==c[1][0] and a2+b2==c[1][1] and a2+b3==c[1][2] and a3+b1==c[2][0] and a3+b2==c[2][1] and a3+b3==c[2][2]:
        print('Yes')
        exit()
print('No')
