ans = 0
for _ in range(2):
    ticket = int(input())
    noriho = int(input())
    ans += min(ticket, noriho)

print(ans)
