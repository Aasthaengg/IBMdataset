n,k=map(int,input().split())
v=list(map(int,input().split()))

result=0

for a in range(min(n,k)+1):
    for b in range(min(n,k)+1-a):
        tmp=v[:a]+v[n-b:]
        tmp.sort()

        lost=k-a-b

        ttt=[]
        cnt=0
        for item in tmp:
            if item<0 and cnt<lost:
                ttt.append(item)
                cnt+=1
            else:
                break
        result=max(result,sum(tmp)-sum(ttt))

print(result)

