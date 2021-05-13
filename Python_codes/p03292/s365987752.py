l = list(map(int, input().split()))
l.sort()
res = 0
for i in range(1, len(l)):
    res += abs(l[i-1]-l[i])
print(res)
