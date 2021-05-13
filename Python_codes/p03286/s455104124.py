n = int(input())
if n == 0:
    print(0)
    exit()
i = 0
ans = []
while abs(n) > 0:
    ans.append(n%2)
    #n = (n - n % (2 * (-1)**i)) // 2
    n = (n - (n % 2)) // -2
    i += 1
print(''.join(map(str, ans[::-1])))
