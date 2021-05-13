n, m= map(int, input().split())
high = list(map(int, input().split()))
ans = [0]*n
 
for i in range(m):
    a,b = map(int, input().split())
    if high[a-1] > high[b-1]:
        if ans[a-1] == 0:
            ans[a-1] = 1
        ans[b-1] = -1
    elif high[a-1] < high[b-1]:
        if ans[b-1] == 0:
            ans[b-1] = 1
        ans[a-1] = -1
    else:
        ans[b-1] = -1
        ans[a-1] = -1
print(ans.count(0) + ans.count(1))