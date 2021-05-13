A = int(input())
ans = 0
listA = []
for i in range(A):
    listA.append(list(map(int,input().split())))
listA = listA[::-1]
for i in range(A):
    if (listA[i][0]+ans) % listA[i][1] == 0:
        continue
    if listA[i][1] == 1:
        continue
    ans += listA[i][1]-(listA[i][0]+ans)%listA[i][1]
print(ans)