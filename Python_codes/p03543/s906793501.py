a,b,c,d=map(int,input()) #1行で連続して入力

if a==b==c or b==c==d or a==b==c==d:
    print('Yes')
else:
    print('No')