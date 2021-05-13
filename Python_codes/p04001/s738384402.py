s = input()
res = int(s)
length = len(s)
for i in range(1, 2**(length-1)):
    res_i = 0
    b = bin(i)[2:].zfill(length-1)
    s_ = s[0]
    idx = 0
    while idx < length - 1:
        for bi in b:
            if int(bi):
                res_i += int(s_)
                idx += 1
                s_ = s[idx]
            else:
                idx += 1
                s_ += s[idx]
    res_i += int(s_)
    res += res_i
print(res)