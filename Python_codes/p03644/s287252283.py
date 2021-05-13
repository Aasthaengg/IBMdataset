n = int(input())
x = 1
for i in range(10):
    x_nxt = x * 2
    if x_nxt > n:
        break
    x = x_nxt
print(x)
