ip = [int(s) for s in input().split(' ')]

h = ip[2] - ip[0]
m = ip[3] - ip[1]

total = (h * 60) + m - ip[4]

if total >= 0:
    print(str(total))
else:
    print(str(0))
