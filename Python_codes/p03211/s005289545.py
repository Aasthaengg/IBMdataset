s = input()

ans_list = []
for r in range(len(s)-2):
    num = int(s[r:r+3])
    ans_list.append(num)

minimum = 10**5
for i in ans_list:
    tmp = abs(753-i)
    if tmp < minimum:
        minimum = tmp

print(minimum)