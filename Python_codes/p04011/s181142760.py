N= [int(input()) for n in range(4)]
if N[0] < N[1]:
    print(N[0]*N[2])
else:
    print(N[1]*N[2]+(N[0]-N[1])*N[3])