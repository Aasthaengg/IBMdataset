#
# 172C Go to school
#
a = []
n = input()
nums = [int(e) for e in input().split()]

for i in range(int(n)):
    a.append([i, nums[i]])

a_sorted = sorted(a, key=lambda x: x[1])

for i in range(int(n)):
    print(str(a_sorted[i][0]+1), end=' ')