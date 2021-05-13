from itertools import accumulate

n=int(input())
au=list(map(int,input().split()))
al=list(map(int,input().split()))

au=accumulate(au)
al=reversed(list(accumulate(reversed(al))))

print(max(x+y for x,y in zip(au,al)))
