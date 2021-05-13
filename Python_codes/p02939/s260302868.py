S = input()

l = len(S)
pre = ''
flag = 0
count = 0

for i in range(l):
    if flag == 1:
        flag = 0
        continue

    try:
        tmp = S[i]
        if tmp == pre:
            flag = 1
            pre = tmp + S[i+1]
            count += 1
        else:
            pre = tmp
            count += 1
    except IndexError:
        pass

print(count)