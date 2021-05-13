a,b,c,d=input()
for i in range(2**3):
    op=["-","-","-"]
    for j in range(3):
        if (i>>j&1):
            op[j]="+"
    if eval(a+op[0]+b+op[1]+c+op[2]+d)==7:
        print(a+op[0]+b+op[1]+c+op[2]+d+"=7")
        exit()