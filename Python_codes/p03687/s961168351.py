def f(s,target):
    cnt = 0
    while len(set(s)) != 1:
        tmps = ""
        for i in range(len(s)-1):
            if s[i] == target and s[i+1] != target:
                tmps += target * 2
            elif s[i] != target and s[i+1] == target:
                tmps += target * 2
            else:
                tmps += s[i]
        cnt += 1
        s = tmps
    return cnt

ans = float('inf')
s = input()
for alp in sorted(set(s)):
    print
    ans = min(f(list(s),alp),ans)
print(ans)