S=input()
L=len(S)
X=('dream','dreamer','erase','eraser')
while L>0:
    f=1
    for x in X:
        if S[:L].endswith(x):
            L-=len(x)
            f=0
    if f:
        break
print(['NO','YES'][L==0])