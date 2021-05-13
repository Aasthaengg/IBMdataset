N = int(input())
d = list(map(int,input().split()))
k = 0
d.sort()
if len(d) % 2 == 1:
    k = 0
elif d[int(len(d) / 2)] == d[int((len(d) / 2) - 1)]:
    k = 0
else:
    k = d[int(len(d) / 2)] - d[int((len(d) / 2) - 1)]

print(k)