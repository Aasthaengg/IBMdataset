n = int(input())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    tot = a+b
    AB.append([a, b, tot])

AB = sorted(AB, key=lambda x:x[2], reverse=True)

a_eat = 0
b_eat = 0

for i in range(n):
    if i%2 == 0:
        a_eat += AB[i][0]
    else:
        b_eat += AB[i][1]

ans = a_eat - b_eat
print(ans)