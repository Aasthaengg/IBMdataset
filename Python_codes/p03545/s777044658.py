s = list(input())
n = len(s)

for i in range(2 ** (n - 1)):
    num = int(s[0])
    num_list = [str(s[0])]
    for j in range(n - 1):
        if (i >> j) & 1:
            num += int(s[j + 1])
            num_list.append("+" + str(s[j + 1]))
        else:
            num -= int(s[j + 1])
            num_list.append("-" + str(s[j + 1]))
    if num == 7:
        [print(t, end="") for t in num_list]
        print("=7")
        break