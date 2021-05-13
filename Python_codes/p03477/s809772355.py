a = list(map(int,input().split()))
A=a[0]
B=a[1]
C=a[2]
D=a[3]

if A+B>C+D:
    print('Left')
elif A+B==C+D:
    print('Balanced')
else:
    print('Right')
