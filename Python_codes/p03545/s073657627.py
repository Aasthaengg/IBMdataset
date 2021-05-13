n = input()
l = len(n) - 1

for i in range(2 ** l):
    ans: int = int(n[0])
    num = n[0]
    for j in range(l):
        if (i >> j) & 1:
            num += "+"
            num += n[j + 1]
        else:
            num += "-"
            num += n[j + 1]
    for k in range(1, len(num), 2):
        if num[k] == "-":
            ans -= int(num[k+1])
        else:
            ans += int(num[k+1])
    if ans == 7:
        print(num + "=7")
        break
