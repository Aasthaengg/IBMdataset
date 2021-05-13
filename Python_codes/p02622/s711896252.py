s = input()
t = input()
if s == t:
    print(0)
else:
    ans = 0
    for i, letter in enumerate(s):
        if letter != t[i]:
            ans += 1
    print(ans)