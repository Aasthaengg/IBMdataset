from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
result = 0
cnt = Counter(a)
cnt_set = set(cnt.items())
cnt_sort = sorted(cnt.items(), key=lambda x:x[1])
for i in range(len(cnt_set) - k):
    result += cnt_sort[i][1]

print(result)