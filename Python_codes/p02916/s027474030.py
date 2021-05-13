n = int(input())
order = list(map(int, input().split()))
satisfaction = list(map(int, input().split()))
addition = list(map(int, input().split()))

index = order[0]
ans = 0

for i in order:
    ans += satisfaction[i-1]
    if i-1 == index:
        ans += addition[i-2]
    index = i

print(ans)