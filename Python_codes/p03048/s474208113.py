M=3000
R,G,B,N=map(int,input().split())

S=0
for x in range(M+1):
    for y in range(M+1):
        c=N-(R*x+G*y)
        if c>=0 and c%B==0:
            S+=1

print(S)
