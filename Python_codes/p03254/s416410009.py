N, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
a.sort()
a_sum = [sum(a[:i+1]) for i in range(len(a))]

for i, item in enumerate(a_sum):
    if x < item:
        ans = i
        break
    elif x == item:
        ans = i+1
        break
    elif x > item and i == len(a_sum)-1:
        ans = i
        break

print(ans)

