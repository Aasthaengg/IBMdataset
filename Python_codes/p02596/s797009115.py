import sys
K=int(input())


if K%2==0 or K%5==0:
    print(-1)
    sys.exit()
    
mod=7%K
if mod==0:
    print(1)
    sys.exit()
    
i=1
while True:
    mod=(10*mod+7)%K
    i+=1
    mod=mod%K

    if mod==0:
        print(i)
        break