n = int(input())

hList = sorted(list(map(int,input().split())))
print(abs(hList[0]-hList[-1]))

