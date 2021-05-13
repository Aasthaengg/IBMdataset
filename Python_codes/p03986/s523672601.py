x = input()
cnt = 0
for x_ in x:
    if x_ == 'T' and cnt:
        cnt -= 1
    elif x_ == 'S':
        cnt += 1
print(2 * cnt)
