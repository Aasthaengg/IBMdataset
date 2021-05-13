N,D=[int(x) for x in input().rstrip().split()]
if N%(1+D*2)==0:
    print(N//(1+D*2))
else:
    print(N//(1+D*2)+1)