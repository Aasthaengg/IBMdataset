def solve(n, m, s):
    cnt = 0
    for i in range(1, n+1):
        if (s[i-1] == "0") and (s[i] == "1"):
            cnt = 1
        elif (s[i-1] == "1") and (s[i] == "1"):
            cnt += 1
        if cnt >= m:
            return -1
    s = s[::-1]
    i = 0
    path = []
    while i < n:
        for j in range(min(m, n-i), 0, -1):
            ni = i+j
            if s[ni] == "0":
                i = ni
                path.append(j)
                break
    return " ".join(map(str, path[::-1]))

n, m = map(int, input().split())
s = input()
print(solve(n, m, s))