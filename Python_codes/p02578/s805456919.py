n = int(input())
a_list = list(map(int, input().split()))

ans = 0
tallest = a_list[0]
for i in range(1,n):
    if tallest > a_list[i]:
        ans += tallest - a_list[i]
    else:
        tallest = a_list[i]

print(ans)
