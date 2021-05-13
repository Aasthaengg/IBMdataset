N = int(input())
arr = list(map(int,input().split()))
ans = []
for i in arr:
    if len(ans) >= i - 1:
        ans.insert(i-1,i)
    else:
        print(-1)
        exit()
for i in ans:
    print(i)