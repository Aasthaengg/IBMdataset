N, M = map(int, input().split())
s = [list(map(int, input().split()))[1:] for i in range(M)]
p = list(map(int, input().split()))
cnt = 0
for a in range(2 ** N):
    flag = 1
    for i in range(M):
        if sum([(a >> (x - 1)) & 1 for x in s[i]]) % 2 != p[i]:
            flag = 0
            break
    cnt += flag
print(cnt)