N,X,T = (int(x) for x in input().split())

time = N//X
if N%X==0:
    print(time*T)
else:
    time += 1
    print(time*T)
