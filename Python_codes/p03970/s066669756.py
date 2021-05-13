a = 'CODEFESTIVAL2016'
cnt = 0
for x, y in zip(input(), a):
    if x != y:
        cnt += 1
print(cnt)