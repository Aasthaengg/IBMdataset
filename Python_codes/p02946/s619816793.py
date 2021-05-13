argList = list(map(int, input().split())) 

outList = [str(x) for x in range(argList[1]-argList[0]+1,argList[1]+argList[0])]
print(" ".join(outList))