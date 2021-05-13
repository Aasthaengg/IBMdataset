M,K=map(int,input().split())
if M==1 and K==1:
    print(-1)
elif M==1 and K==0:
    print(0,0,1,1)
elif K<=(2**M-1):
    r = list(range(2**M))
    r = r[:K]+r[K+1:]
    ans = [K]+r+[K]+r[::-1]
    print(*ans)
else:
    print(-1)