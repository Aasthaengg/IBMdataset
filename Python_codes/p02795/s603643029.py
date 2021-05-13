H=int(input())
W=int(input())
N=int(input())

x = max(H,W)
print((N+x-1)//x)