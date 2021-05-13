a, b, c, d, k = map(int, input().split());

x = 60*a + b
y = 60*c + d

if y>x:
    print(y-x-k);
else:
    print(1440+y-x-k);