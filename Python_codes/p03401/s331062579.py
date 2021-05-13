n = int(input())
list_A = list(map(int, input().split()))
list_A.append(0)
list_A.insert(0, 0)
sum_value = 0

for i in range(1, n+2):
    sum_value += abs(list_A[i]-list_A[i-1])

ans = 0
for i in range(1, n+1):
    min_value = min(list_A[i+1], list_A[i-1])
    max_value = max(list_A[i+1], list_A[i-1])
    if min_value <= list_A[i] <= max_value:
        ans = sum_value
        print(ans)
    else:
        ans = sum_value + abs(max_value-min_value) - abs(list_A[i]-max_value) - abs(list_A[i]-min_value)
        print(ans)