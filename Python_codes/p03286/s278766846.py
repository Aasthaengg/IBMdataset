N = int(input())
out = []
U = 0
D = 0
t = 1
now = 0

if N>0:
    while now!=N:
        X = (N-D)%(2**t)
        if X!=0 and X<=(2**t)//2:
            out.append(1)
        else:
            out.append(0)
        if t%2==1:
            D += 2**(t-1)
        now = 0
        for i in range(len(out)):
            now += out[i]*(-2)**i
        t+=1
if N<0:
    while now!=N:
        X = (U-N)%(2**t)
        if X!=0 and X<=(2**t)//2:
            out.append(1)
        else:
            out.append(0)
        if t%2==0:
            U += -1*2**(t-1)
        now = 0
        for i in range(len(out)):
            now += out[i]*(-2)**i
        t+=1
if N==0:
    out = [0]

print("".join(list(map(str,out[::-1]))))