s = input()
n = len(s)
ret = 753
for i in range(n-2):
    x = abs(753-int(s[i:i+3]))
    ret = min(x, ret)
print(ret)