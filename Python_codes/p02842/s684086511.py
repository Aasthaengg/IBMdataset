# N=1079
N=int(input())

a=int(N*100/110)-1

flg=False

for i in range (N-a+1):
    if ((a+i)*1.08)//1==N:
        print(a+i)
        exit()
    else:
        pass
print(':(')