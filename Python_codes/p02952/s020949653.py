n = int(input())
ret = 0
for i in range(1, n+1):
    if i < 10:
        ret += 1
    elif 10**2 <= i < 10**3:
        ret += 1
    elif 10**4 <= i < 10**5:
        ret += 1
print(ret)