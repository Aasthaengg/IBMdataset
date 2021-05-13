a = int(input())
b = list(map(int, input().split()))
c = {}
d = 1
e = 0
for i in range(1, len(b)):
    if b[i] == b[i-1]:
        d += 1
    else:
        e += d // 2
        d = 1
print(e + d // 2)
