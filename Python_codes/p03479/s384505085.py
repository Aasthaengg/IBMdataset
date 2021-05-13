X,Y=map(int,input().split())

def solve() :
    a=Y//X
    b,n=1,1
    while a>=b :
        b=2**n
        n+=1
    return n-1
  
print(solve())