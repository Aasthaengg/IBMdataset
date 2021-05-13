n = int(input())
a = list(map(int, input().split()))

a.sort()

large = max(a)
a.remove(large)
min_list = [0, large/2]
for i in a:
    if abs(i - large/2) < min_list[1]:
        min_list = [i, abs(i - large/2)]

print(large, min_list[0])
