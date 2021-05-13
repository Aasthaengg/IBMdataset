n = int(input())
argList = list(map(int, input().split()))
ret = argList[0]
#print(argList[0])
for i in range(1,len(argList)):
    #print(min(argList[i-1],argList[i]))
    ret += min(argList[i-1],argList[i])
ret += argList[-1]
#print(argList[-1])
print(ret)