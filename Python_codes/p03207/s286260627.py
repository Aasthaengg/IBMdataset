n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))
ans.sort(reverse=1)
ans[0] = ans[0]//2
print(sum(ans))