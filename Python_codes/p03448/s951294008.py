a = int(input())
b = int(input())
c = int(input())
x = int(input())
cnt = 0
y = x
x_500 = x // 500

for i in range(int(min([x_500+1, a+1]))):
    x = y - i*500
    x_100 = x // 100
    for j in range(int(min([x_100+1, b+1]))):
        x_50 = x // 50
        if x_50 <= c:
            cnt += 1
            x = x - 100
        else:
            x = x - 100
print(cnt)