argList = list(map(int, input().split())) 

ret = argList[2] - (argList[0]-argList[1])

if ret < 0:
    ret = 0
print(ret)