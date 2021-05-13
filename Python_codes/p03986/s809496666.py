x = input()

cnt = 0

while len(x) - 1 > cnt:
    if x[cnt] == 'S' and x[cnt+1] == 'T':
        x = x[:cnt] + x[cnt+2:]
        cnt = max(0, cnt - 1)
    else:
        cnt += 1

print(len(x))
