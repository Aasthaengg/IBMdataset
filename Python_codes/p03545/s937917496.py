s = list(input())

for i in range(2**3):
    ans = ""
    ans += s[0]
    tmp = int(s[0])
    for j in range(3):
        if (i >> j)&1:
            ans += "+" + s[j+1]
            tmp += int(s[j+1])
        else:
            ans += "-" + s[j+1]
            tmp -= int(s[j+1])
    if tmp == 7:
        print(ans+"=7")
        exit()
