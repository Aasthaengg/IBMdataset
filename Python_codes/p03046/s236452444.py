m,k = map(int, input().split())

if k == 0:
    ans = []
    for i in range(1<<m):
        ans.append(i)
        ans.append(i)
elif 1<<m <= k or m==1:
    ans = [-1]
else:
    ans = [i for i in range(1<<m) if i!=k]
    ans = ans + [k] + ans[::-1] + [k]

print(*ans)