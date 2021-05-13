n, t = map(int, input().split())
a = list(map(lambda x: int(x), input().split()))
#a = list(map(lambda x: int(x), in1.split()))
b = []
strlow = a[0]

for idx1 in range(1, len(a)):
    b.append(a[idx1] - strlow)
    if a[idx1] < strlow:
        strlow = a[idx1]

print(b.count(max(b)))
