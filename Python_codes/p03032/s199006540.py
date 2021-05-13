from heapq import heappop,heappush


def main():
    N,K=map(int,input().split())
    Juwels=list(map(int,input().split()))


    res=0

    for l in range(min(N,K)+1):
        for r in range(min(N,K)-l+1):
            hands=[]
            for juwel in Juwels[:l]:
                heappush(hands,juwel)
            for juwel in Juwels[N-r:]:
                heappush(hands,juwel)

            step=l+r
            while len(hands)>0 and step<K:
                value=heappop(hands)
                if value>=0:
                    heappush(hands,value)
                    break
                step+=1

            res=max(res,sum(hands))

    print(res)

if __name__=="__main__":
    main()


