n = int(input())

argList = list(map(int, input().split()))
argList2 = argList.copy()
argList2.sort()

med_before = argList2[int(len(argList2)/2)-2]
med = argList2[int(len(argList2)/2)-1]
med_after = argList2[int(len(argList2)/2)]

for a in argList:
    if( a <= med):
        print(med_after)
    else:
        print(med)