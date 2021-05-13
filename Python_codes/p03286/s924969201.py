n = int(input())
if n == 0:
    print(0)
    exit()
i = 1
ans = []
while n != 0:
    if n % (i*2) != 0:
        n -= i
        ans.append(1)
    else:
        ans.append(0)
    i *= -2
print("".join(map(str,ans[::-1])))