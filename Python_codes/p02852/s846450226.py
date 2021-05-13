from sys import exit

n, m = map(int, input().split())
s = input()[::-1]

res = []
pos = 0
while True:
    if pos + m >= n:
        res.append(n - pos)
        break

    step = m
    while s[pos + step] == '1':
        step -= 1
        if step == 0:
            print(-1)
            exit()
    
    pos += step
    res.append(step)
    
print(*res[::-1])