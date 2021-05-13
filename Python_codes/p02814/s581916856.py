N,M=list(map(int,input().split()))
A=list(map(int,input().split()))

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

fv=A[0]//2
fmod=A[0]

for i in range(1,N):
    sv=A[i]//2
    smod=A[i]

    x,y,gcd=egcd(fmod,smod)
    if sv%gcd!=fv%gcd:
        print(0)
        exit(0)
    fv=fv-fmod*x*(fv-sv)//gcd
    fmod=fmod*smod//gcd
    fv=(fv+fmod)%fmod

if M<fv:
    print(0)
    exit(0)

if fv==0:
    print((M-fv)//fmod)
else:
    print((M-fv)//fmod+1)