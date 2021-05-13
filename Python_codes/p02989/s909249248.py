n = int(input())
d = sorted(list(map(int, input().split())))
t = n//2
if d[t-1] == d[t]:
    print(0)
else:
    print(d[t]-d[t-1])