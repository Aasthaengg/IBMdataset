N=input()
K=input()
N=int(N)
K=int(K)

#初期化
ans=1
counter=0

for counter in range(N):
    #Do A or B
    if ans<=K:
        ans*=2
    else:
        ans+=K

print(ans)