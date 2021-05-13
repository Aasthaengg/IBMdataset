X = input()

s, t = 0, len(X)//2
cnt = 0
used = 0
for x in X:
    if x == 'S':
        s += 1
        if t-used > 0:
            cnt += 1
            used += 1
    else:
        used = max(0, used-1)
        t -= 1

print(len(X)-cnt*2)