n, k = list(map(int, input().split())) 
argList = list(map(int, input().split())) 
argList.sort()
print(sum(argList[n-k:]))