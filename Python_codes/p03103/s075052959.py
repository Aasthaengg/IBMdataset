N, M = map(int, input().split())
AB = [0] * N
B = [0] * N
for i in range(N):
    AB[i] = list(map(int, input().split()))
AB.sort()
price = 0
ans = 0
for i in range(N):
    if M <= AB[i][1]:
        ans += AB[i][0] * M
        break
    ans += AB[i][0] * AB[i][1]
    M -= AB[i][1]
print(ans)
