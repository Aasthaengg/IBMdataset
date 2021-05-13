N,Y=map(int,input().split())

answer=[-1,-1,-1]
for x in range(N+1):    
    for y in range(N-x+1):
        z=N-x-y
        A=Y-10000*x-5000*y-1000*z
        if A==0:
            answer=[x, y, z]

print(*answer)