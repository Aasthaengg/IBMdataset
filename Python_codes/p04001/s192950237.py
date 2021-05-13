S = input()

length = len(S)
ans = 0

for x in range(2 ** (length - 1)):
    res = ""
    b = str(format(x, '010b'))
    for i in range(length):
        res += str(S[i])
        if b[-(i + 1)] == "1":
            res += "+"
        else:
            pass
    ans += eval(res)
        
print(ans)