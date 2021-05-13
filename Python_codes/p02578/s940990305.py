n = int(input())
a = list(map(int, input().split()))
res = 0
temp_max = 0
for x in a:
    if temp_max > x:
        res += temp_max - x
    temp_max = max(temp_max,x)

print(res)