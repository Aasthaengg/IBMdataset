n = int(input())
v = list(map(int, input().split()))

v = sorted(v)
# print(v)
while len(v) != 1:
    a = v.pop(0)
    b = v.pop(0)
    avg = (a+b)/2
    # print(a, b, avg)
    v.append(avg)
    v = sorted(v)

print(v[0])
