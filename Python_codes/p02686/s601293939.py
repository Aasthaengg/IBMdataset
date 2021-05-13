n = int(input())
s = []
for i in range(n):
    temp = input()
    count = 0
    min_count = 0
    for j in temp:
        if j == "(":
            count += 1
        else:
            count -= 1
            min_count = min(min_count, count)
    s.append([count, min_count])
sum_count = sum([s[i][0] for i in range(n)])
if sum_count != 0:
    print("No")
else:
    s2 = [s[i] for i in range(n) if s[i][0] >= 0]
    s3 = [s[i] for i in range(n) if s[i][0] < 0]
    s2.sort(key = lambda x: x[1], reverse = True)
    s3.sort(key = lambda x: x[1] - x[0])
    flag = True
    count = 0
    for i in range(len(s2)):
        if count + s2[i][1] < 0:
            flag = False
            break
        else:
            count += s2[i][0]
    for i in range(len(s3)):
        if count + s3[i][1] < 0:
            flag = False
            break
        else:
            count += s3[i][0]
    if flag == True:
        print("Yes")
    else:
        print("No")