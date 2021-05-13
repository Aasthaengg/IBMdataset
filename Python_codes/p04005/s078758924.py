A,B,C = list(map(int,input().split()))
ans = 0
if A % 2==1 and B%2==1 and C%2==1:
    listA = [A,B,C]
    listA.sort()
    print(listA[0]*listA[1])
else:
    print(0)