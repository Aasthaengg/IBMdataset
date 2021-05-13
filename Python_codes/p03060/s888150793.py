N = int(input())
value_list = list(map(int, input().split()))
cost_list = list(map(int, input().split()))
total = 0
for i in range(N):
    ans = value_list[i] - cost_list[i]
    if ans > 0:
        total += ans
print(total)