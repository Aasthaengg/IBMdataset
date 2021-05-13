N=int(input())
if N%3==0:
    print(N//3)
else:
    print(int((N+3-1)/3)-1)