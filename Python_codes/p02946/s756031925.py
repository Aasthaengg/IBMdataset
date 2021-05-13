k,x=map(int,input().split())
print(*range(max(-1000000,x-k+1),min(x+k,1000001)))