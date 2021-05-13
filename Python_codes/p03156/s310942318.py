import itertools

n = int(input())
a, b =map(int, input().split())
points = list(map(int, input().split()))

cnt = 0
first = []
second = []
third = []
for i in points:
    if i <= a:
        first.append(i)
    elif a+1 <= i and i <= b:
        second.append(i)
    else:
        third.append(i)

ans = min(len(first), len(second), len(third))
print(ans)