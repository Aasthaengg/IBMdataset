n=int(input())
num = list(map(int, input().split()))

def culc(pattern):
    sum=0
    cost=0
    for i in range(n):
        sum+=num[i]
        if i%2==pattern:
            if sum>=0:
                cost+=sum+1
                sum=-1
        else:
            if sum<=0:
                cost+=-sum+1
                sum=1
        #print("sum is ", sum, "cost is ", cost)
    #print("")
    return cost


print(min(culc(0), culc(1)))