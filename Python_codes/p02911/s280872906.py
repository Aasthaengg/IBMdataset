from collections import Counter
n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
count = Counter(a)
ans = [(k - q) for _ in range(n)]

list = ["No" for _ in range(n)]

for key, value in count.items():
    ans[key - 1] = k - q + value
    if ans[key - 1] > 0:
        list[key - 1] = "Yes"

for i in list:
    if k - q > 0:
        print("Yes")
    else:
        print(i)
