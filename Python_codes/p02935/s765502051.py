n = int(input())
v = list(map(int, input().split()))
v.sort()

while len(v) > 1:
    v_tmp = (v[0] + v[1]) / 2
    v.append(v_tmp)
    v.sort()
    v.remove(v[0])
    v.remove(v[1])

print(*v)