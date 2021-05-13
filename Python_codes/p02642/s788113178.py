N = int(input())
As = list(map(int, input().split()))

max_per = max(As)
ansList = [0 for _ in range(max_per + 10)]

for A in As:
    checkList = [i for i in range(A, max_per+1, A)]
    #print(checkList,As)

    for check in checkList:
        ansList[check] += 1

ans = 0

for A in As:
    if(ansList[A] == 1):
        ans += 1

print(ans)