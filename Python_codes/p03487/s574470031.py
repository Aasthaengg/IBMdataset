n = int(input())
a = list(map(int, input().split()))

dict = {}
for i in range(n):
    if a[i] in dict:
        dict[a[i]] = dict[a[i]] + 1
    else:
        dict[a[i]] = 1

total_cnt = 0
for k, v in dict.items():
    a_cnt = 0
    if k > v:
        a_cnt += v
    else:
        a_cnt += (v - k)
    total_cnt += a_cnt
print(total_cnt)