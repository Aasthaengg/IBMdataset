S = int(input())
if S<=10**9:
    print(0,0,0,1,S,0)
else:
    a = S%(10**9)
    x = 10**9
    y = 1
    if a==0:
        z = 0
    else:
        z = 10**9-a
    w = (S+y*z)//(10**9)
    print(0,0,x,y,z,w)