n,c,k = map(int, input().split())
T = []
for i in range(n):
    T.append(int(input()))
T.sort()
ans = 1
last_t = T[0]
passengers = 0
for t in T:
    if last_t +k >= t and passengers < c:
        passengers += 1
    else:
        last_t = t
        passengers = 1
        ans += 1

print(ans)



