def make_map(X):
    X = list(map(lambda x: ord(x) - ord("a"), X))
    s = [-1]*26
    res = [0]+[-1]*(len(X)-1)
    cnt = 0
    for i, x in enumerate(X):
        if s[x] == -1:
            s[x] = res[i] = cnt
            cnt += 1
        else:
            res[i] = s[x]
    return res
print("Yes" if make_map(input())==make_map(input()) else "No")