X = input()

res = 0
l = 0
for x in X:
    if x == 'S':
        l += 1
    elif l > 0:
        res += 1
        l -= 1
print(len(X)-2*res)