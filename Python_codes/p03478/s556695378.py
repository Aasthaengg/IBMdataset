N, A, B = map(int, input().split())
ans = []
for i in range(1, N + 1):
    i = str(i)
    tmp = 0
    for j in range(len(i)):
        tmp += int(i[j])
    if A <= tmp <= B:
        ans.append(int(i))

print(sum(ans))
