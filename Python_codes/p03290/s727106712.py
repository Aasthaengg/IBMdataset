d,g = map(int,input().split())
pc = []
for i in range(d):
    p,c = map(int,input().split())
    pc.append((p,c))
minimum = 2000
for i in range(2**d):
    count = 0
    remain = g
    for j in range(d):
        if i >> j & 1:
            count += pc[j][0]
            remain -= (j+1)*100*pc[j][0]
            remain -= pc[j][1]
    highest = d*100
    while remain > 0 and highest >= 100:
        if not i >> (highest//100-1) & 1:
            if highest * pc[highest//100-1][0] >= remain:
                count += -(-remain//highest)
                remain -= -(-remain//highest)*highest
            else:
                count += pc[highest//100-1][0]
                remain -= pc[highest//100-1][0]*highest
        highest -= 100
    if remain <= 0:
        minimum = min(minimum,count)
print(minimum)