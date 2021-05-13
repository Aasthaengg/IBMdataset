def solve(s):
    n = len(s)
    res = 0
    i = 0
    num = 0
    while i < n-1:
        if s[i] == "A":
            num += 1
            i += 1
        elif s[i:i+2] == "BC":
            res += num
            i += 2
        else:
            num = 0
            i += 1
    return res

s = input()
print(solve(s))