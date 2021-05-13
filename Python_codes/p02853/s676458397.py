x,y = map(int,input().split())

money = [ 300000, 200000, 100000,]
result = 0
if x <= 3:
    result += money[x-1]
if y <= 3:
    result += money[y-1]
if x == 1 and y == 1:
    result += 400000
print(result)