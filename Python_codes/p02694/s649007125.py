X = int(input())
money, cnt = 100, 0
while money < X:
    cnt += 1
    money += money//100
print(cnt)