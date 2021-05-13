l = input().split()
l[0]=int(l[0])
l[1]=int(l[1])
MAX=int(1e+18)

if (l[0] % l[1])==0:
    print(-1)
    exit()

for i in range(1,l[1]):
    if (l[0]*i)>MAX:
        print(-1)
        exit()
    if (l[0]*i)%l[1]!=0:
        print(l[0]*i)
        exit()
