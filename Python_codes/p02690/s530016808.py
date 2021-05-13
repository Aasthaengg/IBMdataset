x = int(input())
x_3zyoukon=x**(1/3)
x_5zyoukon=x**(1/5)

for a in range(int(x_3zyoukon+1)):
    for b in range(a):
        if a**5-b**5==x:
            print(str(a)+" "+str(b))
            exit()

for a in range(int(x_5zyoukon+1)):
    for b in range(-1,(-1)*int(x_5zyoukon+1),-1):
        if a**5-b**5==x:
            print(str(a)+" "+str(b))
            exit()