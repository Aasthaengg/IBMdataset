n = int(input())

F = [0]*50
F[0] = 1
F[1] = 1
if n== 0 or n==1:
    print(F[n])
else:
    for i in range(2,n+1):
        F[i] = F[i-1]+ F[i-2]
    print(F[n])
