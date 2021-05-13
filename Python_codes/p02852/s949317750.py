N, M = map(int, input().split())
S = input()

now = N
ans = []
while now > 0:
    for i in range(M, 0, -1):
        if now-i >= 0:
            if S[now-i] == '0':
                ans.append(i)
                now -= i
                break
            if i == 1:
                print(-1)
                exit()

print(*ans[::-1])


