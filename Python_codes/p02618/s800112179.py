d = int(input())
c = list(map(int, input().split()))

for _ in range(d):
    s = list(map(int, input().split()))
    ret = -20000
    ans = 1
    for i in range(26):
        tmp = s[i] - c[i] * 200
        if ret < tmp:
            ret = tmp
            ans = i + 1
    print(ans)