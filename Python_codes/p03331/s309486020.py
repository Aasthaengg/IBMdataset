N = list(input())
if int(''.join(N))%10 != 0:
    res = 0
    for i in range(len(N)):
        res += int(N[i])
else:
    res = 10
print(res)