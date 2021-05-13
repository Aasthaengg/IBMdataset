n = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))
ans = []
for i in range(n):
    average_tmp = t - H[i] * 0.006
    diff = abs(a - average_tmp)
    ans.append(diff)
print(ans.index(min(ans)) + 1)
