n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))

temp_list = [abs(t - i * 0.006 - a) for i in h]
min_diff = min(temp_list)
for i, temp in enumerate(temp_list):
    if temp == min_diff:
        print(i + 1)
        break