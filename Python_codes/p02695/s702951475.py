import copy

N, M, Q = list(map(int, input().split()))
a = [0] * Q

for i in range(Q):
    a[i] = list(map(int, input().split()))

mscore = 0

def createArray(num,arr):
    global mscore
    arr.append(num)
    if len(arr) < N:
        for i in range(num,M+1):
            arrr = copy.deepcopy(arr)
            createArray(i,arrr)
    else:
        score = 0
        for item in a:
            if arr[item[1]-1] - arr[item[0]-1] == item[2]:
                score += item[3]
        mscore = max(mscore, score)

for i in range(M):
    arr = []
    createArray(i+1,arr)

print(mscore)