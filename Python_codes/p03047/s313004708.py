p=input().rstrip().split(' ')
if int(p[0])==int(p[1]):
    print(1)
elif int(p[1])>int(p[0]):
    print(0)
else:
    print(int(p[0])-int(p[1])+1)
