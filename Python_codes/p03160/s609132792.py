n  = int(input())
k = 2
num = list(map(int,input().split()))
numval = list()
for data in range(n):
    numval.append(1000000000)
numval[0] = 0
i = 0
if(n<k):
    k = n-1
for i in range(0,n):
    for data in range(1,k+1):
        if(i+data)>=n:
            break
        numval[i+data] = min(numval[i+data],numval[i]+abs(num[i]-num[i+data]))
    i += 1
print(numval[n-1])        