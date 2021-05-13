n = int(input())
d = list(map(int, input().split()))
d.sort()
a = n//2
if d[a] == d[a-1]:
    print(0)
    exit()
print(d[a] - d[a-1])