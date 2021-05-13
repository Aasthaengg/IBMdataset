data = []
while True:
    in_line = raw_input()
    if int(in_line) == 0:
        break
    sum = 0
    for s in in_line:
        sum += int(s)
    data.append(sum)
for d in data:
    print d