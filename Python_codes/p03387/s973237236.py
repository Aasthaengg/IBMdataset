a, b, c = map(int, input().split(" "))
max_v = max(a, b, c)
sum_v = a + b + c
cc = 0
if max_v % 2 == sum_v %2:
    cc = (3 * max_v - sum_v) // 2
else :
    cc = (3 * (max_v + 1) - sum_v) // 2

print(cc)