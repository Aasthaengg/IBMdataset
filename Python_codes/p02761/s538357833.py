N, M = map(int, input().split())
index = [i for i in range(1, N + 1)]
cnt = [0] * (N)

dict = dict(zip(index, cnt))

s = [0] * M
c = [0] * M

if M == 0:
    if N == 1:
        print(0)
        exit()
    print(10 ** (N - 1))
    exit()

for i in range(0, M):
    s[i], c[i] = map(int, input().split())
    if s[i] == 1 and c[i] == 0 and N != 1:
        print(-1)
        exit()


for i in range(0, M):
    if dict[s[i]] == 0:
        dict[s[i]] = c[i]
    elif dict[s[i]] == c[i]:
        pass
    else:
        print(-1)
        exit()
# print(dict)
ans = ""
for i in range(1, N + 1):
    if i == 1 and dict[1] == 0 and N != 1:
        ans = ans + "1"
    else:
        ans = ans + str(dict[i])
    # print(ans)

print(ans)
