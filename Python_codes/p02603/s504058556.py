N = int(input())
kabu = [int(i) for i in input().split()]
money = 1000
hoji = 0

for i in range(N-1):
    if kabu[i] < kabu[i+1] and not hoji:
        hoji = money//kabu[i]
        money = money - hoji*kabu[i]
    if kabu[i] > kabu[i+1] and hoji:
        money = money + hoji*kabu[i]
        hoji = 0
if hoji:
    money = money + hoji*kabu[i+1]
print(money)