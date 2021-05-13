n = int(input())
a_i = list(map(int, input().split()))
preval = a_i[0]
cnt = 0
money = 1000
for x in range(1,n):
    val = a_i[x]
    if cnt == 0 and preval < val:
        cnt = money // preval
        money = money % preval
    elif cnt != 0 and preval > val:
        money += cnt * preval
        cnt = 0
    preval = val
if cnt != 0:
    money += cnt * val
print(money)
