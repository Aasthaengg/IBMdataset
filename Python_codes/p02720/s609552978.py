K = int(input())
l = list(range(1,10))

for x in l:
    if x > 3234566667: break
    back = int(str(x)[-1])
    for b in [back-1, back, back+1]:
        if 0 <= b <= 9:
            l.append(10*x + b)

print(l[K-1])