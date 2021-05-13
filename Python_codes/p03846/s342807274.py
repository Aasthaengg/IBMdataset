n = int(input())
s = list(map(int, input().split()))
s_set = set(s)
count = 2 ** ((n) // 2)
if (sum(s) == 2 * sum(s_set)):
    print(count % (10 ** 9 + 7))
else:
    print(0)