x = int(input())
m = 100
t = 0
while m < x:
    n = m // 100
    m += n
    t += 1
print(t)