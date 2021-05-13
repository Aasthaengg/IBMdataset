N,K=map(int,input().split())
syou=N//K
print(min(N-K*syou,abs(N-K*(syou+1))))