s = list(map(int, input().split()))
if (s[1] != 1):
    ans = s[0] - s[1]
    print(ans)
else:
    print(0)