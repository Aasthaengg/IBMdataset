n = input()
a = [int(A) for A in input().split()]

max_ele = 0
for i in range(len(a)):
    if a[i] > max_ele:
        max_ele = a[i]

mid = 0
mid_val = max_ele / 2

for j in range(len(a)):
    if abs(mid_val - a[j]) < abs(mid_val - mid):
        mid = a[j]

print(str(max_ele) + " " + str(mid))