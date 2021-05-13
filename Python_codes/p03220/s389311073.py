n = int(input())
t, a = map(int, input().split(" "))
h = list(map(int, input().split(" ")))
avg_list = []
res = 0
for i in range(0, n):
    avg = t - h[i] * 0.006 - a
    if avg < 0:
        avg = -avg
    avg_list.append(avg)
print(avg_list.index(min(avg_list)) + 1)