n = int(input())
b = list(map(int, input().split()))
l = [""]
for i in b:
    l.insert(i - 1, i)
print(*l[-1] and [-1] or l, sep="\n")