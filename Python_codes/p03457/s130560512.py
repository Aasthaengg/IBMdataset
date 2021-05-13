def end():
    print('No')
    exit()

n = int(input())
t, x, y = [0]*n, [0]*n, [0]*n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())

temp = abs(x[0]) + abs(y[0])
if t[0] % 2 == temp % 2:
    if t[0] < temp:
        end()
else:
    end()

for i in range(1, n):
    temp = abs(x[i]-x[i-1]) + abs(y[i]-y[i-1])
    if (t[i]-t[i-1]) % 2 == temp % 2:
        if t[i]-t[i-1] < temp:
            end()
    else:
        end()

print('Yes')