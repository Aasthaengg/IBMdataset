N,M=map(int,input().split())
print(min(N,M//2)+max(0,(M-(N*2))//4))