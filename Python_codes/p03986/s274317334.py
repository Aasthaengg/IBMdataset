x = input()

cnt = 0
numt = 0
x = x[::-1]
for i in range(len(x)):
    if x[i] == 'T':
        numt += 1
    else:
        if numt > 0:
            cnt += 1
            numt -= 1
print(len(x)-2*cnt)