n=int(input())
a=list(map(int,input().split()))
a.sort()
negative=[]
positive=[]
for ele in a:
    if ele<0:
        negative.append(ele)
    else:
        positive.append(ele)
if len(negative)==0:
    print(sum(a))
else:
    if len(negative)%2==0:
        print(-sum(negative)+sum(positive))
    else:
        if len(positive)==0:
            print(-sum(negative)+2*negative[-1])
        elif -negative[-1]>positive[0]:
            print(-sum(negative)+sum(positive[1:])-positive[0])
        else:
            print(-sum(negative[:-1])+sum(positive)+negative[-1])
