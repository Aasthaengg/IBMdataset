ABC = list(map(int, input().split()))
ABC.sort()
cnt = 0
while not ABC[0] == ABC[1] == ABC[2]:
    ABC.sort()
    if ABC[2] - ABC[0] > 1:
        ABC[0] += 2
        cnt += 1
    else:
        if ABC[0] == ABC[1]:
            ABC[0] += 1
            ABC[1] += 1
            cnt += 1
        else:
            ABC[1] += 1
            ABC[2] += 1
            cnt += 1
print(cnt)