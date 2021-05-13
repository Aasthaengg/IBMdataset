import math
n = int(input())

ans_bool = False
ans_num = 0

for i in range(1, n+1):
    if math.floor(i * 1.08) == n:
        ans_bool = True
        ans_num = i
    else:
        pass
if ans_bool:
    print(ans_num)
else:
    print(":(")
