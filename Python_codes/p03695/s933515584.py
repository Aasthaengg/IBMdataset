n = int(input())
a = [int(x) for x in input().split() if int(x) < 3200]
c = len(set([x // 400 for x in a]))
print(max(c, 1), c + n - len(a))