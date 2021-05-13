N,D = map(int,input().split())
one_per=D*2+1
if(N%one_per!=0):
    print(N//one_per+1)
else:
    print(N//one_per)