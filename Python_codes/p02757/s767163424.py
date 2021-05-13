from collections import defaultdict

n, p = map(int, input().split())
s = input()

if p in (2, 5):
    if p == 2:
        ok_list = [i for i in range(10)][::2]
    else:
        ok_list = [0, 5]
    ans = 0
    for i in range(n):
        if int(s[i]) in ok_list:
            ans += i+1
    print(ans)
else:
    dd = defaultdict(int)
    dd[0] = 1
    prev = 0

    for i in range(n-1, -1, -1):
        d = int(s[i]) * pow(10, n-i, p)
        prev = (prev + d) % p
        dd[prev] += 1

    print(sum(v*(v-1)//2 for v in dd.values()))