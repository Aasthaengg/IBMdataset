k,a,b=map(int,input().split())
if a+1>=b:
    print(k+1)
    exit()
c=k-a+1
if c%2==0:
    print(max(k+1,a+(c//2)*(b-a)))
else:
    print(max(k+1,(c//2)*(b-a)+a+1))