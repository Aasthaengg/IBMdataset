k,a,b=map(int,input().split())
gain=b-a
if gain>=2:
    k-=a-1
    print(a+k//2*gain+k%2)
else:
    print(k+1)