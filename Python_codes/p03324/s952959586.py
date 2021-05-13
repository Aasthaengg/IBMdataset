d, n = map(int, input().split())
x = 100 ** d
y = x
cnt = 0
while cnt < n:
    if y % 100**(d+1) != 0:
        cnt += 1
    y += x
print(y-x)