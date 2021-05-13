import math
def better(l, ans):
    for i in range(2, n):
        ans[i] = min(ans[i - 1] + abs(l[i]-l[i - 1]), ans[i - 2] + abs(l[i]-l[i - 2]))
    return ans
n = int(input())
l = list(map(int, input().split()))
ans = [0] * n
ans[1] = abs(l[1]-l[0])
print(better(l, ans)[len(ans)-1])