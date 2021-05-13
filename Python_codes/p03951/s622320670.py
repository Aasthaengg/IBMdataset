n = int(input())
s = list(input())
t = list(input())


ans = 0
for i in range(n):
    ans = 0
    if t[n - i - 1] == s[-1]:
        for j in range(n - i - 1):
            if s[n - 1 - j] == t[n - i - 1 - j]:
                continue
            else:
                ans = 1
        if ans == 0:
            print(len(s + t[n - i :]))
            break
    else:
        ans = 1
if ans == 1:
    print(len(s + t))