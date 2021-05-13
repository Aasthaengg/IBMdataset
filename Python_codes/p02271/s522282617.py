import itertools

numA = int(input().rstrip())
listA = list(map(int,input().rstrip().split(" ")))
numQ = int(input().rstrip())
listQ = list(map(int,input().rstrip().split(" ")))

sumA = []
cnt = 0


for i in range(1,numA+1):
    tmpComb = list(itertools.combinations(listA, i))
    for nums in tmpComb:
        sumA.append(sum(nums))


for i in range(numQ):
    if sumA.count(listQ[i]) > 0:
        print("yes")
    else:
        print("no")