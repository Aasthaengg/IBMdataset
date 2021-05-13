N=int(input())

a=N//1.08
if int(a*1.08)==N:
    print(int(a))
elif int((a+1)*1.08)==N:
    print(int(a+1))

else:
    print(':(')
