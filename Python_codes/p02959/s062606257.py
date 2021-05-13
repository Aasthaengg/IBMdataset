n = int(input())
M = list(map(int,input().split()))
Y = list(map(int,input().split()))

c=0
np=0
for i in range(n):
    if M[i]<np :
        c+=M[i]
        np=Y[i]
    elif M[i]<Y[i]+np :
        np = Y[i]+np-M[i]
        c+=M[i] 
    else:
        c+=Y[i]+np
        np = 0 
c+=min(np,M[n])

print(c)