n = int(input())
s = [int(input()) for _ in range(n)]
all = sum(s)
if all % 10:
    print(all)
else:
    d = [i for i in s if i % 10]
    if d:
        all -= min(d)
        print(all)
    else:
        print(0)