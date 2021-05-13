H=int(input())
W=int(input())
N=int(input())
c=0
ch=0
cw=0

while c<N:
    if H-cw>W-ch:
        c+=H-cw
        ch+=1
    else:
        c+=W-ch
        cw+=1

print(ch+cw)
