N, T = map(int, input().split())
t = list(map(int, input().split()))
sum = T
before = t[0]
for ti in t[1:]:
    temp = ti-before
    if temp < T:
        sum += temp
    else:
        sum += T
    before = ti
print(sum)