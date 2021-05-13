n,t=map(int,input().split(' '));T=list(map(int,input().split(' ')))
total = 0
tstart, tend = T[0],T[0]+t
i = 1
while i < n:
    if T[i] > tend:
        total += (tend-tstart)
        tstart,tend = T[i],T[i]+t
    else:
        tend = T[i]+t
    i += 1
total += (tend-tstart)
print(total)