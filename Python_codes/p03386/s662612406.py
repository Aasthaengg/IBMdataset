a, b, k = map(int, input().split())
ans_set = set()

for num in range(k):
    if a + num <= b:
        ans_set.add(a + num)

for num in range(k):
    num = k - num - 1
    if b - num >= a:
        ans_set.add(b - num)
for num in sorted(ans_set):
    print(num)
