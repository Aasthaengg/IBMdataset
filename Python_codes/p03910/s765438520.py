n = int(input())

ans = []
check = 0

for i in range(1,n+1):
    check += i
    ans.append(i)
    if check >= n:
        break

if check - n != 0:
    del ans[check - n - 1]
    
for i in ans:
    print(i)