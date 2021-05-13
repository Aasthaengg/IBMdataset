n = int(input())
a = list(map(int, input().split()))
# 4の倍数と2の倍数を数える
four = 0
two = 0
ele = 0
for i in range(n):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0 and a[i] % 4 != 0:
        two += 1
    else:
        ele += 1

"""
ele += two % 2
two = two//2
print(two, end=" ")
print(four, end=" ele=")
print(ele)
if ele <= (two+four) or (ele-(four+two) == 1):
    print("Yes")
else:
    print("No")
"""
if ele <= four:
    print("Yes")
elif ele-four == 1 and two == 0:
    print("Yes")
else:
    print("No")
