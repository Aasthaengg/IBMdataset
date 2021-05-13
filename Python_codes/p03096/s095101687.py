a = int(input())
C = list()
last = [-1] * 2 * 100002
for i in range(a):
    C.append(int(input()))

ans = [1] * a
last[C[0]] = 0
# print(last,ans)
for i in range(1, a):
    ans[i] = ans[i - 1]
    if C[i] == C[i - 1]:
        continue
    if last[C[i]] != -1:
        ans[i] += ans[last[C[i]]]
    last[C[i]] = i

print(ans[a - 1] % 1000000007)