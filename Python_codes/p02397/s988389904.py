a = []
while True:
    x = map(int, raw_input().split())
    if x[0] == 0 and x[1] == 0:
        break
    if x[0] > x[1]:
        tmp = x[1]
        x[1] = x[0]
        x[0] = tmp
    a.append([x[0], x[1]])
for i in range(len(a)):
    print a[i][0], a[i][1]