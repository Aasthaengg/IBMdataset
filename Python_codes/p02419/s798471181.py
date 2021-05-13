W = input()
cnt = 0
while 1:
    line = input()
    if line == "END_OF_TEXT":
        break
    line = line.lower().split()
    for P in line:
        if P == W:
            cnt += 1
print(cnt)