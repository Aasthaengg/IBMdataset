N,M=map(int,input().split())

ans=M//N
while True:
    if (M-(N-1)*ans)%ans==0:
        break
    ans-=1
print(ans)