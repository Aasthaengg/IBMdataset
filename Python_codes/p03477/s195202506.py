
[A,B,C,D] = list(map(int,input().split()))
L,R = A+B, C+D

if L==R:
    print('Balanced')
elif L>R:
    print('Left')
else:
    print('Right')