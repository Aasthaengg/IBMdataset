a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a%10==0:
    A=a
else:
    A=((a//10)+1)*10
if b%10==0:
    B=b
else:
    B=((b//10)+1)*10
if c%10==0:
    C=c
else:
    C=((c//10)+1)*10
if d%10==0:
    D=d
else:
    D=((d//10)+1)*10
if e%10==0:
    E=e
else:
    E=((e//10)+1)*10
    
time=A+B+C+D+E
muda=[]
muda.append(A-a)
muda.append(B-b)
muda.append(C-c)
muda.append(D-d)
muda.append(E-e)
print(time-max(muda))