n = int(input())
k = int(input())
ans = [1]
for i in range(n):
    if ans[i] < k:
        ans.append(2*ans[i])
    else:
        ans.append(ans[i] + k)
print(ans[n])