N = int(input())
B = list(map(int, input().split()))
ans = []
for i in range(N):
    if i == 0:
        ans.append(B[0])
    elif 0 < i < N - 1:
        temp = min(B[i - 1], B[i])
        ans.append(temp)
    elif i == N - 1:
        ans.append(B[-1])
# print(ans)
print(sum(ans))
