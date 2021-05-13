A,B,C,D=map(int,input().split()) #1行で1スペースあけて入力


l=A+B
r=C+D

if l>r:
    print('Left')
elif r==l:
    print('Balanced')
else:
    print('Right')