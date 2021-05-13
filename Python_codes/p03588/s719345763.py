n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort()
a=ab[-1][0]
b=ab[-1][1]
print(a+b)