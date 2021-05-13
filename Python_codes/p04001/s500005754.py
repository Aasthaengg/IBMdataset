s = input()
n = len(s)-1
if n == 0:
    print(s)
    exit()

ans = 0
for i in range(2**n):
    data = []
    for j in range(n):
        if((i >> j) & 1):
            data.append(1)
        else:
            data.append(0)
    # print(data)
    num = s[0]
    x = []
    for i in range(n-1):
        if data[i] == 1:
            x.append(int(num))
            num = s[i+1]
        else:
            num += s[i+1]
    if data[-1] == 0:
        num += s[-1]
        x.append(int(num))
    else:
        x.append(int(num))
        x.append(int(s[-1]))
    ans += sum(x)
    # print(x)
print(ans)
