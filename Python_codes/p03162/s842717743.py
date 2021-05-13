n = int(input())
ans = [[0]*3 for xxx in range(n)]
for i in range(n):
    a,b,c = list(map(int, input().split()))
    if i==0:
        ans[0][0] = a
        ans[0][1] = b
        ans[0][2] = c 
        continue
    ans[i][0] += max(ans[i-1][1], ans[i-1][2]) + a
    ans[i][1] += max(ans[i-1][2], ans[i-1][0]) + b
    ans[i][2] += max(ans[i-1][0], ans[i-1][1]) + c
ans = ans[-1]
print(max(ans))