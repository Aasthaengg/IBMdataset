n = int(input())

ans = []
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if j == n-i and n%2 == 1: pass
        elif j == n-i+1 and n%2 == 0: pass
        else:
            ans.append([i, j])

print(len(ans))
[print(ans[i][0], ans[i][1]) for i in range(len(ans))]