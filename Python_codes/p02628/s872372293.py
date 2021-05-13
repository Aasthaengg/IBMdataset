l = input().split()
n1 = int(l[0])
n2 = int(l[1])

money = input().split()

for i in range(n1):
    money[i] = int(money[i])

money.sort()

ans = 0

for i in range(n2):
    ans += money[i]

print(ans)