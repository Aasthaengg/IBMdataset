from collections import Counter

n = int(input())
c = Counter(list(map(int, input().split())))

ans = 0
for k, v in c.items():
    if k == 0:
        if n%2==0 and v > 2:
            print(0)
            exit(0)
        elif n%2==1 and v > 1:
            print(0)
            exit(0)
    else:
        ans += 1
        if v > 2:
            print(0)
            exit(0)

print(pow(2, ans, 10**9+7))
