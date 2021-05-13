#5B-can you solve this
N, M, C = map(int, input().split())
listB = list(map(int, input().split()))
cnt = 0

for i in range(N):
    sum = 0
    listA = list(map(int, input().split()))
    for j in range(M):
        sum += listA[j] * listB[j]
    if sum + C > 0:
        cnt += 1

print (cnt)