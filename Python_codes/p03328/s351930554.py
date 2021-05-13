a, b = map(int, input().split())
temp = 0
bar_heights = []
for i in range(1, 1000):
    temp += i
    bar_heights.append(temp)

for i in range(1, 499501):
    if (a + i) in bar_heights and \
       (b + i) == bar_heights[bar_heights.index(a + i) + 1]:
        print(i)
        break
