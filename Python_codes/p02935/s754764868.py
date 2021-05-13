N = int(input())
v = sorted(list(map(int, input().split())))
while len(v) > 1:
    temp1 = v.pop(0)
    temp2 = v.pop(0)
    temp = (temp1 + temp2) / 2
    v = sorted([temp] + v)
print(v[0])
