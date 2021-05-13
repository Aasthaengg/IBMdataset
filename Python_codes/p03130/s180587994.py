listA=[]
import collections 
for i in range(3):
    B = list(map(int,input().split()))
    listA.append(B[0])
    listA.append(B[1])
listA=collections.Counter(listA)
listA = listA.most_common()
if listA[0][1] == 2 and listA[1][1] == 2 and listA[2][1] == 1 and listA[3][1] == 1:
    print("YES")
else:
    print("NO")