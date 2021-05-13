a, b, k = map(int, input().split())
# print(f"{a} {b} {k}")

# l = []
# for i in range(a, b + 1):
#     l.append(i)
# print(l)

# l_small = set()
# for i in range(a, a + k):
#     l_small.add(i)
# print(l_small)

# l_large = set()
# for i in range(b, b - k, -1):
#     l_large.add(i)
# print(l_large)

# l = [i for i in range(a, b + 1)]
# print(l)

l_ans = set()

count = 1
for i in range(a, b + 1):
    if count <= k:
        l_ans.add(i)
    else:
        break
    count += 1

count = 1
for i in range(b, a - 1, -1):
    if count <= k:
        l_ans.add(i)
    else:
        break
    count += 1

for num in sorted(l_ans):
    print(num)