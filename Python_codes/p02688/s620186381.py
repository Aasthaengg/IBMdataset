n,k = map(int,input().split())
temp = [False for i in range(n)]
for i in range(k):
    x = int(input())
    y = list(map(int,input().split()))
    for j in y:
        if not temp[j-1]:
            temp[j-1] = True

ans = 0
for i in temp:
    if not i:
        ans += 1
print(ans)