def solve(s, count, i, p):
    if count == 3:
        p = list(p.split(":"))
        if int(p[0]) + int(p[1]) > int(p[2]) and int(p[1]) + int(p[2]) > int(p[0]) and int(p[0]) + int(p[2]) > int(p[1]) :
            return 1
        else:
            return 0

    if i == len(s):
        return 0

    if s[i] in p:
        return solve(s, count, i + 1, p)
    else:
        return solve(s, count + 1, i + 1, p + s[i] + ":") + solve(s, count, i + 1, p)


n = int(input())
l = list(input().strip().split(" "))
q = ""
print(solve(l, 0, 0, q))
