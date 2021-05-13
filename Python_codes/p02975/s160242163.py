from collections import Counter
n = int(input())
s = Counter(list(map(int, input().split())))

if s[0] == n:
    print("Yes")
elif len(s) == 2 and s[0] == n // 3:
    print("Yes")
elif len(s) == 3:
    res = 0
    num = set()
    for k, v in s.items():
        res ^= k
        num.add(v)
    if not res and len(num) == 1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
