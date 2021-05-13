A,B,N=map(int,input().split())
def floor(x):
    return int(A*x/B)-A*int(x/B)
print(floor(min(B-1,N)))